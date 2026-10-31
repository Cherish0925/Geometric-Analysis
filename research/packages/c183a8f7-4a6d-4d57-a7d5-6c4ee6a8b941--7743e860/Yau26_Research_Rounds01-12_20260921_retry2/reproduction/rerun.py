#!/usr/bin/env python3
"""Rerun the finite calculations, without old Sessions or the Qiushi CLI.

Python 3.12 and sympy==1.14.0 were used for the accompanying results.
Exit zero means these programs terminated successfully, not that the
geometric arguments in the research manuscripts were mechanically proved.
"""

import argparse
import concurrent.futures
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import time


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--proof-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--jobs", type=int, choices=(1, 2), default=2)
    args = parser.parse_args()
    root = args.proof_dir.resolve(strict=True)
    scripts = sorted(root.glob("*.py"))
    if not scripts or args.timeout < 1:
        parser.error("Supply a proof directory with scripts and a positive timeout.")
    args.output.mkdir(parents=True, exist_ok=False)
    output = args.output.resolve()
    env = os.environ.copy()
    env.update({name: "1" for name in (
        "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
        "NUMEXPR_NUM_THREADS")})
    env["PYTHONHASHSEED"] = "0"
    worker = (
        "import resource,runpy,sys;"
        "resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3));"
        "resource.setrlimit(resource.RLIMIT_CPU,(int(sys.argv[2]),int(sys.argv[2])+1));"
        "runpy.run_path(sys.argv[1],run_name='__main__')"
    )

    def run(script):
        start = time.monotonic()
        command = [sys.executable, "-I", "-c", worker,
                   str(script), str(args.timeout)]
        try:
            result = subprocess.run(command, cwd=root, env=env,
                                    capture_output=True, text=True,
                                    timeout=args.timeout)
            stdout, stderr = result.stdout, result.stderr
            status = "completed" if result.returncode == 0 else "failed"
            code = result.returncode
        except subprocess.TimeoutExpired as exc:
            def decode(value):
                return value.decode(errors="replace") if isinstance(value, bytes) else value or ""
            stdout, stderr = decode(exc.stdout), decode(exc.stderr)
            status, code = "timeout", None
        elapsed = round(time.monotonic() - start, 3)
        (output / (script.stem + ".txt")).write_text(
            stdout + ("\nSTDERR:\n" + stderr if stderr else ""), encoding="utf-8")
        record = {"script": script.name, "sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
                  "status": status, "exit_code": code, "seconds": elapsed,
                  "log": script.stem + ".txt"}
        print(f"{status:9} {script.name} ({elapsed}s)", flush=True)
        return record

    import sympy
    import mpmath
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
        records = list(pool.map(run, scripts))
    summary = {
        "scope": "Fresh execution of packaged finite calculations; not a proof of the analytic or global topological theorems.",
        "environment": {"python": platform.python_version(), "sympy": sympy.__version__,
                        "mpmath": mpmath.__version__, "platform": platform.system()},
        "limits": {"jobs": args.jobs, "wall_seconds_per_script": args.timeout,
                   "cpu_seconds_per_script": args.timeout, "address_space_gib": 4},
        "total": len(records), "completed": sum(r["status"] == "completed" for r in records),
        "records": records,
    }
    (output / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    return 0 if summary["completed"] == summary["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

"""Record the unchanged local upload snapshot and current proof references."""

from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
SNAPSHOT = ROOT / "line1_sources_20260923"
ORIGINAL = Path("/data/qiushi/research/Yau26_第一科学主线")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    entries = []
    for path in sorted(SNAPSHOT.iterdir()):
        if path.name == "manifest.json":
            continue
        source = ORIGINAL / path.name
        assert source.is_file() and sha(path) == sha(source), path
        entries.append({"name": path.name, "bytes": path.stat().st_size,
                        "sha256": sha(path)})
    assert len(entries) == 7
    duplicates = {}
    for entry in entries:
        duplicates.setdefault(entry["sha256"], []).append(entry["name"])
    proof_paths = ["round3_monopole_input.md", "round4_rigidity.md",
                   "round5_rigidity.md", "round13_chamber.md",
                   "round17_integral.md", "round21_analytic.md",
                   "lebrun_stability_closure.md"]
    proofs = [{"path": name, "sha256": sha(ROOT / name)} for name in proof_paths]
    result = {
        "date": "2026-09-23",
        "original_directory": str(ORIGINAL),
        "baseline_commit": "046166b",
        "current_entry": "../line1_unified_v2.md",
        "files": entries,
        "byte_identical_groups": [names for names in duplicates.values() if len(names) > 1],
        "local_proof_sources": proofs,
        "state_update": "Round13 and Round21 originals available; closure is conditional on the core calibration proof.",
        "history": "Source bytes unchanged, including superseded status sentences; current guidance is the v2 entry.",
    }
    output = SNAPSHOT / "manifest.json"
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(f"Verified {len(entries)} source files and {len(proofs)} local proof references.")


if __name__ == "__main__":
    main()

# Source discovery for the permanent Yau26 library

1 October addition: the complete September 29--30 two-web increment is
preserved in [its own source tree](../archive/sources/20261001-web-increment/),
including the original outer ZIP, both nested source packages, the separately
downloaded note, and all 102 extracted files. The
[source-to-section index](../catalog/web_increment_20261001.json) connects
them to the [current manuscript](../paper/Integral_Einstein_Rigidity.tex).
`python3 tools/library.py find QUERY` also searches this new index.
The source discoveries below retain their original dates and scope.

26 September addition: two complete discussion texts are now preserved under
guidance/source: the [assistant's research priorities](../guidance/source/20260926_assistant_priorities.zh.md)
and the [web analysis supplied by the user](../guidance/source/20260926_user_web_backbone.zh.md).
Their provenance is the present conversation, not a newly recovered external
file or independent mathematical review. Duplicate delivery of the web text
is stored once. The [merged reading entry](../guidance/LINE1_CURRENT.md)
connects both to actual proofs and separates conclusions from research targets.
The original 23 September discovery report below remains historical.

Discovery date: 23 September 2026. Research baseline:
`29f7d2cef30f2ccdba192acdcd02bf516d850fe8`, from
`/data/qiushi/runtime/build/yau26-line1-global-20260923-7t1AtQ`.

This note identifies original materials that a permanent library must preserve.
It does not reclassify old claims as proved, certify every proof, or change an
installed Skill. The machine-readable copy allowlist is
[`catalog/discovery-roots.json`](../catalog/discovery-roots.json). Its source
paths are archival provenance, not portable dependencies for future research.

## 1. The main discovery

The latest integrated tree contains **884 tracked files** and carries the
scientific proof chain through the recent gauge, energy-window and no-bubbling
results. It is not a complete archive of the original research process.
The principal additional sources are:

| Source layer | Material not replaced by the integrated papers |
| --- | --- |
| Original user2 Sessions S0910A01–A03 | Working notes, proof programs, experimental data, plans, Codex work, original briefing uploads, deliverables and exported Meta-Trace |
| Historical September 10–17 mathematical packages | Earlier proof versions, corrections, source maps, extracted Fable report/programs, Session record books and finite-check evidence |
| Research uploads and downloads | Human-authored or web-assisted guidance, supplied LaTeX sources, external coverage review, exported packages |
| Later parallel worktrees | A small number of precursor proof variants not byte-identical to the integrated version |
| Installed and immutable Skill copies | Provenance of what the research agents could read; most current copies are exact duplicates of the baseline Skill |

These layers should remain separate. A corrected current proof, its historical
precursor, the human research guidance, and an external review have different
roles even when they discuss the same theorem.

## 2. Original Session sources

The exact original roots exist under
`/data/qiushi/qiushi_engine_v08/users/user2/Sessions/`:

| Session | Notes | Programs | Data files | Briefing files | Deliverables |
| --- | ---: | ---: | ---: | ---: | ---: |
| S0910A01 | 107 | 193 | 111 | 3 | 17 |
| S0910A02 | 89 | 198 | 201 | 3 | 17 |
| S0910A03 | 167 | 221 | 171 | 144 | 17 |

These are filesystem counts at discovery, not mathematical result counts.
Additional scientific material is in `workspace/plans`, `figures`, `proofs`,
`codex_loop/work`, the Markdown reports/proposals in `codex_loop/archive`, and
`trace/exports/meta_trace`. The corresponding v09 scientific subsets were
compared by relative-path SHA-256 and agree with v08. Preserve both origin
identities, but store identical content once if the archive supports deduplication.

The prepared successor Sessions S0917A01–A03 also exist in both versions.
Each has three briefing files and sixteen deliverables, but no notes or scripts
in the inspected directories. This is an observed artifact state, not a claim
about service execution state. Their three research-goal prompts also survive
in `runtime/build/yau26-session-prompts-20260917-foyWtD`.

### Important original uploads in S0910A03

The briefing directory preserves more than the latest three-line summaries:

- `Yau26_uniform_gap.tex` and the accompanying coverage/revision note;
- `Yau26_source_package/`, including the original synthesis source and curation;
- `Yau26_parallel_progress/`, with September 15 timeline, status and withdrawals;
- `Yau26_第26题_完整逐步研究归档_2026-09-16/`, with the full step ledger,
  artifact inventory, detailed derivations, corrections and source-access note;
- `Yau26_三主线科学续接稿_2026-09-16/`, including all three original TeX files;
- `Yau26_三条科学主线_完整综合稿_2026-09-17/`, containing the three original
  rigidity, construction and global manuscripts;
- `yau26_3mainline.md`;
- `yau26_verification_artifacts/`, including the Fable report, 39 original
  checking programs and retained output records.

The integrated `skill/references/source-coverage.json` already records identities
for many of these. That is not the same as embedding the original files.
The permanent archive should now retain their bytes, not only their names.

The Fable source report contains corrected or withdrawn assertions. In
particular, its claimed implication from W to a fixed closed counterexample
must not be retrieved as a current theorem. Preserve the source unchanged and
link its affected sections to the retained scale/volume correction. Likewise,
retain the distinction between sampled profile constants and certified uniform
bounds, and between one failed sign branch and failure of the whole working
Yau26 statement.

## 3. Skill snapshots: what is and is not missing

All fourteen installed `qiushi-yau26` directories were compared to baseline
`skill/`, using SHA-256 for each relative non-hidden file:

- v08: `admin`, `user1` through `user10`;
- v09: `admin`, `user1`, `user2`.

Every inspected installed tree has **243 files**, with no missing, extra or
changed non-hidden file relative to the baseline Skill. Thus these installations
do not contain another unintegrated mathematical version. The instance-root
`Skills/` directories themselves are empty.

Immutable built-in Skill sources exist at:

| Platform asset version | Files | Relation to baseline |
| --- | ---: | --- |
| `1f-20260917.yau26.1/skills/qiushi-yau26` | 20 | Earlier mathematical snapshot |
| `1f-20260921.yau26.1/skills/qiushi-yau26` | 241 | Earlier integrated snapshot |
| `1f-20260921.yau26.2/skills/qiushi-yau26` | 243 | Byte-identical by relative path |

These paths are below `/data/qiushi/runtime/platform-assets/`. Their catalog
entries say `default_context_enabled=false`; this discovery did not test GUI
activation or alter it. Copy only the named Skill subtree, not the platform
catalog, authentication or installation machinery.

## 4. Historical runtime material

A bounded content-hash comparison of mathematical text, programs, data,
archives and rendered papers against the current baseline found:

1. The round 2–21 proof/program bodies are already retained in the integrated
   tree. Several early round `README.md` files differ and are useful historical
   state records, not additional theorems.
2. The September 10–17 `package/` trees retain earlier versions. The
   `qiushi-yau26-flat-20260916-6fHNZy/record-books/` directory retains the three
   Session record books, and `mathematical-results/` retains additional finite
   computation output.
3. The early reference package preserves the primary problem-source PDF
   `two_major_open_problem_list.pdf`, as well as `Yau26_Research_Dossier.tex`
   and its source manifest. The primary statement must remain distinguishable
   from the project's working formulation.
4. The Fable build preserves the extracted original material and its isolated
   checking records. Its original source is also present in the Session upload;
   retain path aliases for byte-identical copies.
5. The following parallel-worker notes have content variants absent from the
   baseline and should be retained as **historical precursors**, not rival
   current theorem statements:
   `line1_conformal_neck.md`, `line1_canonical_shear.md`,
   `line1_ricci_remainder.md`, `line1_non_kahler_bridge.md`,
   `line1_yamabe_endpoint.md`, the earlier integral-rigidity manuscript,
   and the pre-integration Bauer–Furuta/no-bubbling drafts.

The machine-readable allowlist supplies each exact source root and relative
file pattern. It deliberately does not copy whole generic engine trees or
readiness-test workspaces. Operational publication/readiness records are not
mathematical proof sources.

## 5. Research uploads, reviews and unavailable originals

`/data/qiushi/research/Yau26_第一科学主线/` contains seven original guidance/source
files. Preserve all seven, including the correction that cscK equality does
not imply Einstein equality. Keep their original Chinese wording alongside
English scientific navigation; a translation or condensation must not erase
the supplied source.

The named top-level Yau26 ZIPs in `/data/qiushi/research/` are real local files.
They cover the twelve-round integration, first-line literature package, and
successive September 23 research exports. Retain their original hashes even
when all unpacked mathematics is also archived.

`/home/ubuntu/下载/Skill3_覆盖审计_20260921.md` is byte-identical to the integrated
`skill/references/skill3-coverage-audit-20260921.md`:
`6911bc2996aa9395db6e1d555b861bd4fef06d90fbbb1ea621b4470c6fce7fbe`.
The downloaded dossier TeX is present; its PDF is a distinct rendering from
the early runtime PDF and should retain its own provenance.

Two source gaps remain explicit:

- The later three titles `从统一间隙到更广Einstein判定`,
  `跨尺度匹配与新闭拓扑`, and `同一光滑流形与原题闭合` are named in the Skill3 review,
  but their original files were not located in the checked roots. The earlier
  September 21 trio is present and integrated; it must not be relabelled as
  these later originals.
- The quoted web review's `Yau26_十二轮研究_原稿审读与更新判断_2026-09-21.md`
  and `Yau26_十二轮研究_审读与复算证据_2026-09-21.zip` were not located locally.
  The user's quoted review is available as conversation evidence; this is not
  verification of the absent original files or independent rerun logs.

## 6. Copy and interpretation rules

For every archived regular file, retain source identity, original relative and
absolute paths, byte size, SHA-256, and before/after stat information. A changed
file must be retried or reported; do not call a moving source a stable snapshot.
Do not follow symlinks outside the declared root.

Keep current mathematics, original sources, historical variants, checks and
human guidance as separate navigable layers. Hash equality permits storage
deduplication, not theorem deduplication; distinct hashes do not prove distinct
mathematics. Compilation and check logs retain their original scope.

Exclude credentials, private Runtime state, Session databases/configuration,
lock files, worker identity, caches and unrelated research. The allowlist omits
raw trace contexts, `context_slots.json` and duplicate OCR-asset caches; it
retains exported scientific Meta-Trace and original scientific documents.

This discovery closes a concrete source-preservation gap. It does not justify
claiming that every historical conversation or third-party file has been found,
nor that every inherited mathematical assertion has been independently proved.

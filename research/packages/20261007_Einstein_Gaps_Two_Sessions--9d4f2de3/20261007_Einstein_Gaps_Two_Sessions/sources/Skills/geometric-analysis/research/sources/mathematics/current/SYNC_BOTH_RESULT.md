# Yau 26 Skill synchronization: v08 and v09

21 September 2026. The user authorized updating both systems while retaining
prior research assets. No mathematical content was changed in this operation.

## Installed result

All eleven existing v08 users were updated with the existing extension-package
installer. The three existing v09 users were already current and were rechecked.
All fourteen have 241 files with tree digest:

`62eada6cf238285346f7acf69fe47a3d836f9fc7f75627c3b4e1b8ec38af8818`

The source is
`/data/qiushi/runtime/releases/qiushi-yau26-research-1f-20260921.1/skills/qiushi-yau26`.

Before replacement, every v08 target matched the approved previous digest.
The owning installer archived each previous package during its atomic exchange.
After installation, all fourteen current trees and previous archive payloads
were hash-validated. A detached copy of an archived package was restored under
`/tmp/yau26-backup-recovery-ylbdtw13/qiushi-yau26` and independently validated.
No previous package was deleted. Built-in installation receipts were unchanged.

Evidence:

- `validation/v08-plan.json`: bounded pre-install inspection.
- `validation/v08-applied.json`: actual eleven-user update and archive IDs.
- `validation/both-installations.json`: current and archived hashes for all
  fourteen users, plus the detached recovery test.
- `package_tools/verify_both_installations.py`: reproducible read-only check.

## Future-user onboarding boundary

Independent read-only inspection confirmed both running GUI processes still
select `/data/qiushi/runtime/platform-assets/1f-20260917.yau26.1`.
The prepared `/data/qiushi/runtime/platform-assets/1f-20260921.yau26.1` preserves
the other four assets byte-for-byte and provides Yau Skill version 7 with
`default_context_enabled=false`.

There is no supported hot replacement of the process environment. The
configuration owners are:

- v08: `/home/ubuntu/.config/systemd/user/qiushi-engine-v08-8103.service.d/75-yau26-builtin.conf`.
- v09: `/data/qiushi/qiushi_engine_v09/deploy/1f-v09/launch.sh`, whose export
  takes precedence over a systemd environment value.

Neither launch configuration was changed and neither service was restarted.
At the next authorized GUI deployment, change these catalog selections to the
prepared directory and test new-user installation. Until then, users created
after this synchronization still receive the older built-in Yau package.
Existing users retain the current update because their previous built-in
receipts were deliberately left unchanged.

This operation did not modify Session goals, progress, model settings, selected
Skills, research files, databases, unrelated assets or service state.

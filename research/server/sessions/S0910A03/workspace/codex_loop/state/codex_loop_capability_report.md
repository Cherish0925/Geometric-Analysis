# Codex Loop Capability Report

- **updated_at**: `20260911_134208`
- **status**: `ok`
- **status_meaning**: ok means the mandatory runtime checks passed and provider authentication is not known to be missing or failed. Provider authentication is verified only after a successful Codex run.
- **runtime_status**: `ok`
- **provider_auth_status**: `verified`
- **provider_auth_verified**: `True`
- **provider_auth_updated_at**: `20260911_121950`
- **codex_version**: `codex-cli 0.153.4`
- **model**: `gpt-5.6-sol`
- **model_reasoning_effort**: `xhigh`
- **runtime_sandbox_model**: Outer bubblewrap enforces the real read/write boundary; Codex exec/goal is launched with its internal sandbox bypassed to avoid double-sandbox conflicts.
- **codex_home_agents_exists**: `True`
- **approval_policy**: ``
- **sandbox_mode**: ``
- **network_access_configured**: `true`
- **dns_config_ok**: `True`
- **venv_python_ok**: `True`
- **readonly_user_write_blocked**: `True`
- **codex_loop_write_allowed**: `True`
- **runtime_ready**: `True`

## Capability Warnings

- none

## Codex Skills

- `imagegen` (system)
- `openai-docs` (system)
- `plugin-creator` (system)
- `review-agent` (system)
- `skill-creator` (system)
- `skill-installer` (system)

## MCP Servers

- `openaiDeveloperDocs`

## GPU / ML Device Visibility

- **CUDA_VISIBLE_DEVICES**: `0,1`
- **nvidia_smi_available**: `True`
- **nvidia_smi_query_ok**: `True`
- **gpu_names**: `NVIDIA H100, NVIDIA H100`
- **torch_import_ok**: `True`
- **torch_cuda_available**: `True`
- **torch_cuda_device_count**: `2`

## Python Packages

### ai_ml

- import ok: `accelerate`, `anthropic`, `datasets`, `openai`, `peft`, `sentence_transformers`, `torch`, `torchaudio`, `torchvision`, `transformers`
- missing/import failed: none

### documents_images

- import ok: `PIL`, `bs4`, `cv2`, `fitz`, `imageio`, `lxml`, `pdfplumber`, `pypdf`, `skimage`
- missing/import failed: none

### optimization_math

- import ok: `casadi`, `cvxpy`, `jax`, `jaxlib`, `pulp`
- missing/import failed: none

### scientific_core

- import ok: `matplotlib`, `networkx`, `numpy`, `pandas`, `scipy`, `seaborn`, `sklearn`, `statsmodels`, `sympy`, `tqdm`
- missing/import failed: none

### testing

- import ok: `hypothesis`, `pytest`
- missing/import failed: none


## System Tools

### core_shell

- available: `awk`, `bash`, `date`, `env`, `file`, `find`, `grep`, `head`, `readlink`, `realpath`, `rg`, `sed`, `sh`, `sort`, `stat`, `tail`, `tee`, `timeout`, `uniq`, `wc`, `xargs`
- missing: none

### gpu_ml_system

- available: `nvcc`, `nvidia-smi`
- missing: none

### image_media

- available: `compare`, `convert`, `ffmpeg`, `ffprobe`, `identify`, `montage`
- missing: `inkscape`, `magick`, `rsvg-convert`

### latex_pdf

- available: `biber`, `bibtex`, `gs`, `latexmk`, `lualatex`, `pandoc`, `pdfinfo`, `pdflatex`, `pdftocairo`, `pdftoppm`, `pdftotext`, `xelatex`
- missing: `mutool`, `qpdf`

### math_proof

- available: `Singular`, `cvc5`, `gap`, `gp`, `lake`, `lean`, `maxima`, `qiushi-wolfram-run`, `qiushi-wolfram-status`, `sage`, `z3`
- missing: `wolframscript`

### network_data

- available: `curl`, `rsync`, `scp`, `ssh`, `wget`
- missing: none

### software_build

- available: `cmake`, `g++`, `gcc`, `make`, `ninja`, `node`, `npm`, `npx`, `pip`, `pkg-config`, `python`, `python3`
- missing: `cargo`, `clang`, `clang++`, `go`, `rustc`, `uv`

### version_control

- available: `git`
- missing: none


This inventory is measured from inside the Codex loop sandbox. Skills are instruction packs; MCP servers must be configured in .codex_loop_home/config.toml; Linux/Python tools are command-line resources available to Codex when it works under codex_loop. The listed commands are a capability summary, not a closed list; Codex may use other local tools visible in PATH.

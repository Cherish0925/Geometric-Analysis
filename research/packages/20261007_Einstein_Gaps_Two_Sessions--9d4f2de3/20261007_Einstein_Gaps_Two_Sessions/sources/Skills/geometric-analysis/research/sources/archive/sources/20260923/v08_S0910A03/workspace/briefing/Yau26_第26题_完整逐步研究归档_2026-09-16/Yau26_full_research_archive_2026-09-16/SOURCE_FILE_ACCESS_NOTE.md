# Source file access note

本次 ZIP 直接打包本次生成文件与当前 `/mnt/data` 中可访问的旧总结。File Library/求是引擎服务器里的文件是“引用对象”，当前 Python sandbox 没有其 raw bytes，因此不能诚实地直接复制。

未直接嵌入 raw bytes 的主要对象：
- meta_trace_report (93)(1).md
- meta_trace_report (94)(1).md
- meta_trace_report (95)(1).md
- Yau26_Ricci_pinching_research.md
- Yau26_synthesis.tex / .pdf
- 求是引擎服务器 `workspace/notes`, `scripts`, `data`, `proofs`

本归档已经保存它们的数学内容、关键推导、Step 1–100 合并账本、artifact paths、theorem status 和 supersession 关系。

若需要 bit-for-bit 原始工程归档，需要将这些 File Library/服务器文件挂载或上传到当前会话后再次打包。

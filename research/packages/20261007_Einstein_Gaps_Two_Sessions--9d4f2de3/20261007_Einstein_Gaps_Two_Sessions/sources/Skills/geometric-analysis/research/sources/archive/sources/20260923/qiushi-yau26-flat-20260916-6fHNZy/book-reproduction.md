<a id="reproduction"></a>

# 五、脱离原会话读取与复算

## 已内置什么

三个底本保存实际研究目录中的文字笔记、数学代码、形式化源文件、参数和结果、研究计划及全部300步的研究交接；被数学笔记直接引用的支持论证也一并收录。网页上传的科学续接稿、详细归档、进展包及修訂说明保留原文。完全相同的底本正文只存一次，并保留各来源入口。

正文中的旧 `Sessions/...` 路径是来源标识。打开对应的本地Markdown链接即可读到内容；无需旧Session存在。三份专题的可提取完整TeX也保存在底本内，避免Markdown呈现取代原公式源代码。历史两稿及统一间隙证明另以原始TeX保存。

常规文献引用仍指向公开论文。没有把整篇外部论文、下载HTML、重复OCR、运行日志、模型原始对话或编译缓存当作本项目成果塞进研究正文。尚未实际取得的文献或手稿保持原来的来源状态；例如归档提到但没有上传全文的 `Yau26_Ricci_pinching_research.md`，没有凭摘要补造。

## 大型重复网格的处理

A01第4步的Taub–Bolt边界CSV是一份约16.6 MB的机械采样网格，没有单独复制每一行。本Skill完整保留生成程序 `step4_taub_bolt_boundary_probe.py`、其参数、公式、`step4_taub_bolt_ads_summary.json`及研究笔记。原程序可重新生成该CSV和图。这里保留的是科学内容与复算方法，不把重复网格行数当作额外研究成果。其他纳入的文字程序和结果均按记录的原始字节保存。

## 提取内置原文

底本每个来源有完整路径、字节数、SHA256与固定起止标记。下面的读取函数只读取本目录，不访问原会话、不执行程序，也不写文件：

```python
from pathlib import Path
import hashlib
import re

def embedded_source(research_dir, source_path):
    for book in sorted(Path(research_dir).glob('S0910A0*.md')):
        content = book.read_bytes()
        heading = ('### ' + source_path + '\n').encode()
        pos = content.find(heading)
        if pos < 0:
            continue
        section_end = content.find(b'\n<a id=', pos + len(heading))
        section = content[pos:section_end if section_end >= 0 else len(content)]
        match = re.search(rb'<!-- BEGIN_SOURCE (source-[0-9a-f]+) bytes=(\d+) -->\n', section)
        if match is None:
            alias = re.search(rb'\]\(#(source-[0-9a-f]+)\)', section)
            if alias is None:
                raise ValueError('No source body or duplicate target')
            start = content.index(b'<a id="' + alias[1] + b'">')
            section = content[start:]
            match = re.search(rb'<!-- BEGIN_SOURCE (source-[0-9a-f]+) bytes=(\d+) -->\n', section)
        start = section.index(b'\n', match.end()) + 1  # skip opening code fence
        payload = section[start:start + int(match[2])]
        expected = re.search(rb'SHA256[^`]*`([0-9a-f]{64})`', section[:match.start()])[1]
        if hashlib.sha256(payload).hexdigest().encode() != expected:
            raise ValueError('Source checksum mismatch')
        return payload
    raise FileNotFoundError(source_path)

# Example: print the complete mathematical proof record, without old Sessions.
source = 'Sessions/S0910A01/workspace/notes/step100_chirality_cancellation_proof.md'
print(embedded_source('.', source).decode('utf-8'))
```

需要运行程序时，先将相应程序和依赖数据提取到新的研究工作区，按源码中明确的输入、路径和软件依赖复算；不要向原路径写回。代码中的历史绝对路径和工作目录需要适配副本。数值结果保持其精度与算法范围，符号恒等式、有限枚举、形式化小命题与全局几何证明分别使用。

## 独立使用的边界

此文集用于完整保存并继续已实际提供的研究，不把未完成的数学接口改写成完成。它保留足以重新检查关键论证的全文和计算依据；软件依赖、公开文献定理及仍待解决的新数学问题不会因打包而消失。原始会话与上传资料没有被删除：独立副本的验收，不应靠先销毁原件来完成。

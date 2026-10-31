# Ricci 夹逼与 Einstein 度量

这是 Yau 26 相关累计研究的主题化整理稿。正文为中文，包含数学证明、构造、技术估计、来源和适用边界。

- `Yau26_synthesis.tex`：完整、独立的 LaTeX 源码，不依赖本地章节路径或外部图片。
- `Yau26_synthesis.pdf`：编译后的阅读版。
- `CURATION.md`：去重、修正、条件降级与累计内容的覆盖说明。

## 编译

使用 XeLaTeX。标准 TeX Live 安装需要包含 `ctex`、Fandol 字体及源码导言区列出的常用宏包。连续编译两次以生成目录和交叉引用：

```sh
xelatex -interaction=nonstopmode -halt-on-error Yau26_synthesis.tex
xelatex -interaction=nonstopmode -halt-on-error Yau26_synthesis.tex
```

源码文件的注释和标签可用于定位主题。公式按章编号；文献链接置于使用相应结果的位置。

## 数学状态

本文不是一般 Yau 26 问题的完整证明或反例，也没有认证会话内推导的文献首创性。经典结果、给定假设下的直接推导、尚未闭合的条件接口均在正文中区分。尤其不能将无复结构、某种平滑失败或某个对称构造族无解，替换成全部 Einstein 度量不存在。

本稿沿用累计研究中的归一化工作问题；原始题页的完整量词未获核准，不把工作版本当作原题逐字引文。

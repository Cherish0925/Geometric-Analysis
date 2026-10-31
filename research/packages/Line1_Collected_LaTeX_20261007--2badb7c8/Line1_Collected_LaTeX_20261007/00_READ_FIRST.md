# 第一科学主线：近期研究补充与证明汇编

整理日期：2026-10-07。

## 入口

`00_Collected_Research.tex` 是一份独立、可编译的完整总稿，包含七章正文及参考文献；不需要通过 `\input` 读取其他 TeX 文件。编译后的阅读本为 `00_Collected_Research.pdf`，共 42 页。

`01_` 至 `07_` 是七份各自独立可编译的专题文件。系统集中审读时可以只读取总稿；分工审读时使用专题文件及其直接前置。各分卷 PDF 在 `pdf_preview/`。

## 七个专题

1. `01_Framework_and_Inputs.tex`：统一记号、N1 的有限参数回接与类平方成本、精确共形比较、有限密度 FD，以及其秩一 Chern 配对引理；明确哪些是继承输入。
2. `02_External_Methods.tex`：openai/math 第342族的正密度流分裂与原流—残余流配对、第351族的核—余核保留、幂—对数展开及路径选择；准确列明向 O10/O11 迁移时未满足的条件。
3. `03_Quantitative_Ricci_Flow.tex`：全度量正无迹 Ricci 间隙、负 Yamabe 与外部四维延拓定理的完整组合证明；标量阈值时间、历史峰值增长及原平衡族的 O(h^{-1}) 推论。
4. `04_Uniform_Endpoints_and_Tower_Recovery.tex`：N1＋有限密度 FD 的地理分区闭合；混合吹起—添柄及已供给多主体的统一端点；预定残余塔安放、完整复制、原 P 证书与稳定混合单元费用。
5. `05_Analytic_CH_Collar_Construction.tex`：显式光滑三轴族、完整相对曲率代价、两尺度因子化、负对数项及 O_R(ε²) 余项、任意固定小领口与固定基底覆盖序列。
6. `06_Two_Orientation_Global_Gap.tex`：曲面丛的两个真实规范类、同一 Hodge 极化的交叉关系、反取向固定 B=2 端点矛盾；Einstein 与 Kodaira 推论。该卷明确以 FD2 为非经典解析前置。
7. `07_Global_Synthesis_and_Remaining_Problems.tex`：系统的已认证便宜单元、一般背景响应、非球商 KE 转移、Nijenhuis/Weyl 节省公式，以及必须保留的错误修正和未闭合连接。

## 数学地位

本套文件是最近各轮材料的编纂，不是新一轮证明认证。完整保留了来源中的命题、推导、几何条件、常数依赖及极限次序。经典供给、项目前置、外部新定理、条件性推论和候选接口分别标明。

一般无密度 O10 与 O11 的真实最优首项尚未由这些文件全部解决。相应族上的严格次四构造已存在，不能继续把“首项必须为4”列为待证真结论。附带的早期来源按原字节保存，其中历史状态必须按第7卷及最新构造更新。

## 编译

建议使用具有 CTeX 的 TeX Live 发行版和 XeLaTeX。例如：

```bash
xelatex -interaction=nonstopmode -halt-on-error 00_Collected_Research.tex
xelatex -interaction=nonstopmode -halt-on-error 00_Collected_Research.tex
```

每个分卷可使用同一方式单独编译。字体配置含 Noto/Fandol 与 TeX Gyre 的回退；不附带字体文件。引用已嵌入每份 TeX 的 `thebibliography`，编译不要求运行 BibTeX；`references.bib` 另供项目合并使用。

## 来源与检查

`SOURCE_INDEX.md` 给出来源及章节对应；`SOURCE_MANIFEST.json` 保存直接来源原件的路径、大小及 SHA-256。`source_notes/` 保留 18 个直接来源、证明前置和原区间回执，不复制整个月的大型研究档案。

总稿与七份分卷均已实际完成三次 XeLaTeX 编译。最终日志未发现未定义引用、重复标签、缺失字形或超宽正文盒；另对总稿进行了 PDF 渲染检查。编译记录见 `COMPILATION_CHECK.json`。这些排版检查不等同于数学正确性认证。

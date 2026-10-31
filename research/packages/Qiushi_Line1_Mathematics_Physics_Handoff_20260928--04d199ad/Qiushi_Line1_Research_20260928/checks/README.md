# 文件与有限代数检查

本目录的脚本用 SymPy 精确运算检查交接稿中的13项有限代数关系，包括 Einstein 残差的最小化与方差分解、四维曲率手性块归一化、一般实二形式的 Maxwell 应力恒等式、总缺陷下界的代数吸收、无迹物质阈值、一圈流去整体尺度投影及四维缩放。

运行：

```bash
python -m pip install sympy
python checks/verify_algebra.py
```

本次运行13项均通过；采用符号恒等式，不使用浮点容差。

5份独立 LaTeX 文件已经使用 XeLaTeX 编译并复跑交叉引用检查。交接稿合并版的封面、目录、公式页和表格页已抽样渲染检查，全部页面文本边界也经过程序检查。TeX 源文件使用 CTeX/Fandol 及 Latin Modern 字体，不附带字体文件；完整 TeX Live / MiKTeX 安装中缺包时需安装相应标准包。

编译示例：

```bash
xelatex -interaction=nonstopmode -halt-on-error '00_完整交接稿.tex'
xelatex -interaction=nonstopmode -halt-on-error '00_完整交接稿.tex'
```

上述检查验证的是文件可编译性与有限公式的一致性，不验证 I40/I41 的解析证明、全部原稿的正确性或物理目标的原创性。对应数学命题仍以第四份文件所列原稿及完整证明为依据。

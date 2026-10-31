# 复现说明

`exact_identities.py` 只用 Python 标准库，以有理系数稀疏多项式验证替换比较、共形平方分解、单解标量恒等式及常数。运行 `python3 exact_identities.py`。

其余四个 Python 文件需要 NumPy、SciPy。在本目录运行，模块之间通过相对同目录导入。`radial_identity_check.py` 用随机种子7及两档积分精度，独立核对实际残差积分与新共形平方恒等式；运行 `python3 radial_identity_check.py`。

`radial_search_new.py`、`radial_constraint_new.py`、`radial_constraint_triaxial.py` 是本轮实际搜索源代码。参数、系数、优化器返回状态与细积分复核保留在三个 JSONL 文件中。`radial_constraint_new.py` 的先行双轴实验终值见附录正文；没有把原始终端日志装入包。

数值返回全部高于4；有无约束随机起点达到迭代上限。这些结果不是全局最优证书，不是全类下界证明，也不是新的低成本构造。小数不是严格区间包络；积分一致性仅用于筛选与实现复核。

本包没有重跑或声称复现输入审读包中的六份旧数值回执；这里交付的是本轮新增程序与结果。

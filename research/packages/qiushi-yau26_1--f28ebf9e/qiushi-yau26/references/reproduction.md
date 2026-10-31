# 独立计算与复现

这里的程序随 Skill 提供输入，不读取旧 Session、Knowledge、网络或其他用户目录。
它们从定义重新计算指定的代数与局部曲率量；四节点组单独检查保存矩阵的解释，
不假装重新计算无穷谱。完整分析证明仍见 [研究正文](../research/20260916.md)。

## 运行

在当前用户根目录，通过已有数值环境运行：

```bash
qiushi-yau26 env numeric python Skills/qiushi-yau26/scripts/reproduce.py --output Sessions/<session_id>/workspace/data/yau26-reproduction-NEW
```

也可以用有 SymPy、NumPy 的 Python 直接运行 `scripts/reproduce.py`。
输出目录必须是新路径；通过 `run_shell` 或 `bg_task` 调用时，为输出父目录声明
`write_paths` 的 `kind=directory`。程序只写指定结果目录，不写 Skill。

默认运行五组。只运行一组时增加 `--group four_node`，或重复 `--group` 选取多组。
每组生成一个 JSON，`manifest.json` 记录依赖版本、输入摘要、结果及耗时。
退出码 0 表示所选检查通过，1 表示至少一项失败，2 表示参数或输出路径不合要求。
检查不用可被 `python -O` 关闭的 `assert`。已有输出目录不会被覆盖。

## 每组具体检查什么

| 组 | 从什么重算 | 得到什么；不代表什么 |
| --- | --- | --- |
| `uniform_gap` | 完成平方、校准密度、Noether 比值、Weyl 特征值与旧 SW 比率消元 | 精确复核 109、436、675、42 等系数及其条件；不代替 Cheeger–Tian、局部展开与极限传递的分析证明，不计算非显式的间隙常数 γ。 |
| `weyl10` | 自对偶和反自对偶两块的十个独立 Weyl 张量，完整 Ricci 线性化 | 逐方向验证曲率对称性、Bianchi、无迹/无散度/调和/径向规范；对任意径向二阶 jet 验证对数插值恒等式。不是只代入几个幂函数，也不验证全局拼接的非线性余项。 |
| `ed_ricci` | 曲面丛移动标架的结构方程，经 Koszul 公式算联络、曲率及全部 Ricci 分量 | 检查混合分量、二次项、标量曲率和相应矩阵谱；不从局部公式推出全局光滑拼接或该流形的 Einstein 不存在性。 |
| `cz_spike` | 尖峰函数全部一、二阶导数，以及相反翘曲的完整移动标架曲率 | 精确验证 Ricci 中 Hessian 相消和 Riemann 中混合导数保留，检查非零背景能量；另作明确网格范围内的数值诊断，不把采样值当全域界或区间证书。 |
| `four_node` | 包内历史截断矩阵、源/接收端坐标变换、五行节点图 | 正确地区分迹、无迹对角、非对角响应，检验必要不等式与有限矩阵系数。不是谱重算，不提供谱尾界，不证明完整 Lyapunov–Schmidt 系统或全局 Einstein 障碍。 |

程序在 [reproduce.py](../scripts/reproduce.py) 与
[math_checks.py](../scripts/math_checks.py)，四节点输入在
[four_node_fixture.json](../scripts/data/four_node_fixture.json)。
原研究程序、参数和历史输出仍在 [计算附录](computations.md) 与
[实验附录](experiments.md)，按程序名可定位；相关错误在原段落附近有修正。

### 四节点输入与归一化

历史矩阵存储的是输入 `(S22,S33,2*S23)` 到输出 `(R22,R33,R23)` 的映射。
第三个输入含系数 2，因为对称张量的两个非对角指标共同参与缩并。
迹、无迹对角、非对角三个实际张量的 Hilbert–Schmidt 范数均为 √2，输入为
`(1,1,0)`、`(1,-1,0)`、`(0,0,2)`。对保存的相邻矩阵，应分别得到
`0`、`(2q,-2q,0)`、`(0,0,-2q)`。不能用第一项的零值检验第二项的非零系数。

保存的十进制矩阵作为回归输入精确读取；这不使原来的截断谱近似成为精确谱值。
五行是固定正背景下的一种相容模式及四种混合模式；节点置换保持方形邻接关系。
不据此把整体手性反转宣称为完整几何等价，也不声称枚举了所有带标记填充。

### 尖峰的能量和数值范围

保留历史参数 `rho=0.30`、`Lambda=5,10,20,50,100,200,500` 和
`sigma=exp(-Lambda)`、振幅 `Lambda^(-2/3)`。本程序使用 384×64 的内盘网格，
积分下限为 `max(sigma/10,1e-14)`，没有计入更小核心及截断环带。
中心值另用精确公式计算，不依赖该网格。

小的扰动 Hessian 能量不意味着固定区域内背景曲率消失。按完整四指标曲率范数，
闭流形 `S²×S²` 上有 `∫|Rm|² = 128π² + 4∫|Ric°|²`；全能量不能趋零。
局部小球的背景能量可以通过先缩小球来控制，不能与同一个固定球上的扰动极限混淆。

## 故障检查

每组都主动输入一个错误变体并要求它被拒绝，例如改错校准系数、漏掉混合 Ricci
分量、反转混合导数符号或丢掉非对角缩并的 2。四节点还提供命令行失败用例：

```bash
qiushi-yau26 env numeric python -O Skills/qiushi-yau26/scripts/reproduce.py --group four_node --mutation four-node-zero --output Sessions/<session_id>/workspace/data/yau26-reproduction-bad-NEW
```

此命令必须返回 1，JSON 必须写 `failed`，不能因为矩阵全为零就算通过。
重复使用已有输出目录必须返回 2。正常与故障实测结果见
[本次复算结果](reproduction-results.json)。

这些程序提供关键计算的独立复现入口，不要求所有研究采用计算路线。
继续开展新证明、构造、文献核查及新的验证方法，不受上述五组检查限制。

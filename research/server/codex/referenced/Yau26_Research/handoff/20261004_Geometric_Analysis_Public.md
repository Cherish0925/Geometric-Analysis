# Geometric Analysis：公共研究 Skill 与计算环境

2026-10-04。

此前整理的完整数学文本库已经保留并转为公共 Skill；不是只复制最新的
O10／O11 文件。连续英文稿、证明与构造、来源索引、知识图、网页增量和修订关系
均保留。新增部分是数学工具接口和可修改的计算例子，不改动原有数学结论。

## 研究时使用

在 Qiushi 用户工作区读取：

- `Skills/geometric-analysis/SKILL.md`：数学主题与按问题选路。
- `Skills/geometric-analysis/references/research-map.md`：完整研究脉络。
- `Skills/geometric-analysis/references/computational-tools.md`：工具、用法与例子。
- `Skills/geometric-analysis/research/Curvature_Realizability.tex`：连续英文数学稿。

统一计算入口：

```bash
qiushi-geometry info
qiushi-geometry examples
qiushi-geometry env sage python geometry.py
qiushi-geometry env tensor cadabra2 tensors.cdb
qiushi-geometry env topology python topology.py
qiushi-geometry env pde python weak_form.py
qiushi-geometry lean statement.lean --declaration theorem_name
```

计算程序与输出保存在当前 Session 或项目中，不写入共享软件或公共来源正文。
公共 Skill 不限定一种未来证明路线，也不把尚开放的问题变成已证定理。

## 本机状态

v08、v09、v07、v04 的36个现有用户工作区已获得 Skill；v08 user2 的
S1003A01、S1003A02 可直接使用上述相对路径和命令。没有启动或修改这两个会话。

新增 Cadabra 2.5.14、Regina 7.4.1、SnapPy 3.3.2、Gmsh 4.15.2 与 meshio；
复用 Sage/SageManifolds、SymPy/NumPy/SciPy/Arb、PDE/MPI、CAPD、Lean/mathlib、TeX。
实际数学算例及 Qiushi 隔离执行入口已验证。Wolfram 许可证已过期，未作为必要依赖。

v08/v09 的新用户自动配给配置在下次服务正常启动时加载；现有用户的 Skill 已安装。
本次没有重启服务。旧系统 v04/v07 的新用户创建机制未改，不能把这次现有用户分发
理解为旧系统全部生命周期已经迁移。

## 长期维护

[公共 Skill 源码](/data/qiushi/local_git/worktrees/geometric-analysis-public-20261004/system/skills/geometric-analysis/SKILL.md)
与[数学运行组件](/data/qiushi/local_git/worktrees/geometric-analysis-public-20261004/system/tools/geometric-analysis/README.md)
在 Qiushi 本地 Git 管理。新数学仍在本研究工程中形成，再更新公共文本库；
公共软件依赖通过新版本环境升级，不逐用户重复安装。

[开发记录](/data/qiushi/local_git/worktrees/geometric-analysis-public-20261004/knowledge/notes/geometric-analysis-20261004/README.md)
保存环境版本、实际测试、内置资产目录与后续升级方式。本轮只在本服务器准备，未部署其他服务器。

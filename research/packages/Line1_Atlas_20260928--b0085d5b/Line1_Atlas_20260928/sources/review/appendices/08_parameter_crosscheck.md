# audit_parameter.md §2–4 独立交叉核验

对照：第五卷 I40 §4.1–4.3；第七卷原始 Lemma5.1 的精确 Hessian 恒等式及 polynomial divergence coercivity；第一卷 I51 的常权重同解分解。

## 判断

在 I51(2.9a) 的同解恒等式以及已保留的 Hessian/Bianchi 恒等式下，§2–4 的减假设推导闭合。未发现隐含的 smoothing allowance、非恒定权重可解性或不同解之间的比较。它说明 **负 Yamabe 代表上的一个普通实际 SW 解足以供应这条证明**。它不自动构造新的全度量拓扑供给实例，也不关闭 O10/O11。

## 检查细节

1. 常权重2方程有 `|F_A^+|²=rho²/2`，因此 `32pi²p=4 integral rho²−8J`。积分 Weitzenböck 给 `K=integral(rho−rho²/2)`，直接展开可验证

`16K+4 integral(rho−2)²+8J =16V−32pi²p=Sigma`.

精确恒等式(A)没有使用额外曲率估计。

2. beta=2 下 I51(2.9a) 控制 amp²、J、zeta² 和 `W+−W0`。取单调截断 eta(rho) 的局部测试具有原稿写出的符号：

`integral eta |nabla Phi|² = integral eta rho(1−rho/2) −(1/2) integral eta' |d rho|²`.

由于 eta' 有界、支持rho<=3/2，且该支持上 `(rho−2)²>=1/4`，右侧为 O(D)。这是对全局 kinetic identity 的合法局部替代，未把积分等式误作点态。

3. 曲率模型 `F_b Phi` 的系数可由原 I40 模型直接对照。令旧校准振幅变量 rho_old 与新变量关系为

`rho_new=sqrt(3/2) rho_old`.

旧模型的 `rho_old²/4+1/3−sqrt(6)rho_old/4` 恰变为

`rho_new²/6+1/3−rho_new/2 = (rho_new−1)(rho_new−2)/6`；

旧 transverse `rho_old²/8−1/3` 恰变为

`rho_new²/12−1/3 = (rho_new−2)(rho_new+2)/12`.

故它在rho=2湮灭所选spinor，且在0<=rho<=2的全范围满足 `|F_b Phi|²<=C(rho−2)²`。不需要除以rho，不要求spinor无零点。

4. 第七卷 Hessian 精确式含 `Ric(nablaPhi,nablaPhi)`、`F(nablaPhi,nablaPhi)` 与 `|F Phi|²`，没有微分曲率。分裂 `Ric=−g+Ric°`、`F=F_b+(F−F_b)` 后，有界模型部分费用 CK；误差部分由 `||nablaPhi||_4²<=C||nabla²Phi||_2` 吸收，`F_b Phi` 由上一步收费D。由此(E)有效，无额外V项。

5. `B<=2K+C(P+D)+4pi²Y` 的系数也正确：Chern–Weil给 `B<=P/2+Sigma/8−D/9+J+4pi²Y`，而 `Sigma/8=2K+O(D)`。之后 Hessian budget 为 `C(K+Pi+Y)`。

6. 常标量 s=−4 使 contracted Bianchi 的标量导数项为零。其弱形式对任意光滑 tensor 有

`|integral <div W(W0),Z>|<=C(sqrt(P)+||W+−W0||_2)||nabla Z||_2`.

取Z为同一模型散度即可。W0是boundedPhi的四次平行多项式，其二阶导数只支付 Hessian 和 gradient^4，不需要 commutation 或 W− 的额外预算。因此(F)没有隐藏几何常数。

7. 原 bounded-form coercivity的 t=1/8 版本缩放到t=1/2时，J²增大16倍，正好得到

`(1/4)v(|nabla omega|²+|d omega|²)<=|J_W|²+(1/3)|dv|²`.

rho>1上由Hopf身份收费K，rho<=1由局部测试收费D，合起来闭合Young吸收。全程是同一个实际spinor。

8. 共形转移量核对：`P−Phat=delta/12`，`D−Dhat=3delta/2`，故 `Pi−Pihat=19delta/12`。p共形不变；a²与T+拓扑不变。因此 §4 的转移没有额外权重量词。

## 适当表述

可称“同解分解导出的输入削弱命题”，其证明依赖明确、闭合。全度量结论的应用仍须逐共形类提供 Yamabe 代表上的普通解；某一个共形类的存在不能推出其它类的存在。应将‘新定理’的范围限定于该分析输入的削弱，勿据此宣布新的拓扑障碍实例或一般零端完成。

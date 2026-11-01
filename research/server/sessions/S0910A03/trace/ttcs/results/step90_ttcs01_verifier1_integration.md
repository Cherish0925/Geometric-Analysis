# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 90,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step90_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step90_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify and strengthen the Step 90 structured forced free-T^2 reduction. Read the Step 89 derivation, its verifier, and the two new symbolic outputs/scripts. Check in the established H^2 normalization whether Q=(1/2)e^{-3σ}q^T M^{-1}q satisfies Hess_H Q=Qh and |grad_H Q|^2=Q^2; whether the fixed-charge twist source is S_F=-grad_H Q; and whether <dU,D S_F>=-Qe+3<dσ,<grad Q,dU>> plus a term linear in dq. Verify the exact invariant coefficient/norm relating dq to mixed Ricci defect and the round-cusp physical law w'+3w=forcing. Then derive the strongest valid Bochner or combined-energy inequality available without treating variable Q as constant. Keep inf Q (curvature), sup/source norms, and separator average distinct. State plainly whether the +Qe base term cancels, whether any further cancellation with the area equation is available, and what remains unresolved for a complete forced-twist obstruction. Do not extrapolate beyond the free-T^2 class.

## Integrated Scientific Memo

# Step 90 验证结论：强迫 free-\(T^2\) 扭率约化

以下均限于 free \(T^2\)-不变度量。令
\[
G=\rho M,\qquad \rho=e^\sigma,\qquad \det M=1,
\]
并采用既定归一化
\[
h_{\mathbb H^2}=d\alpha^2+e^{-2\alpha}d\beta^2,\qquad
Q=\frac12e^{-3\sigma}q^TM^{-1}q .
\]

## 1. 电荷势结构完全成立

在 Iwasawa 坐标
\[
M=
\begin{pmatrix}
e^\alpha+\beta^2e^{-\alpha}&\beta e^{-\alpha}\\
\beta e^{-\alpha}&e^{-\alpha}
\end{pmatrix},
\]
有
\[
Q=\frac12e^{-3\sigma}
\left[e^{-\alpha}(q_1-\beta q_2)^2+e^\alpha q_2^2\right].
\]
直接计算给出
\[
\boxed{\operatorname{Hess}_{\mathbb H^2}Q=Qh_{\mathbb H^2}},
\qquad
\boxed{|\nabla_{\mathbb H^2}Q|^2=Q^2}.
\]
`step90_charge_potential_verify.json` 的相应残差均为零。

垂直无迹 Einstein 方程的扭率源为
\[
\boxed{S_F=-\nabla_{\mathbb H^2}Q}.
\]
在 \(M=I,\ q=(q_0,0)\) 的标准点，
\[
Q=\frac12e^{-3\sigma}q_0^2,\qquad S_F=Q\,\partial_\alpha,
\]
与 \(L\alpha=Q\) 一致。该等式由约化方程的 \(SL(2,\mathbb R)\)-协变性推广至一般 \(M,q\)。

## 2. \(DS_F\) 的精确结构

设
\[
u_i=dU(e_i),\qquad e=\sum_i|u_i|^2,\qquad
X:=\sum_i \sigma_i\langle\nabla Q,u_i\rangle .
\]
由 \(\operatorname{Hess}Q=Qh\) 及 \(Q,S_F\propto e^{-3\sigma}\)，
\[
D_US_F[u_i]=-Qu_i,\qquad
D_\sigma S_F[\sigma_i]=3\sigma_i\nabla Q.
\]
故允许 \(q\) 变化时
\[
\boxed{
\langle dU,DS_F\rangle=-Qe+3X+R_q,
}
\]
其中
\[
R_q=\sum_i\left\langle u_i,D_qS_F[\nabla_iq]\right\rangle
\]
严格线性依赖 \(dq\)。

定义不变量
\[
|b|^2=e^{-3\sigma}\gamma^{ij}M^{ab}
(\nabla_iq_a)(\nabla_jq_b).
\]
标准点计算并由协变性推广得到
\[
\boxed{\sum_i|D_qS_F[\nabla_iq]|^2=2Q|b|^2},
\qquad
\boxed{|R_q|\le\sqrt{2Qe}\,|b|}.
\]

### 对 exchange 脚本的重要修正

脚本 JSON 中
\[
|X|\le |d\sigma|\sqrt{Qe}
\]
是错误的。因为 \(|\nabla Q|=Q\)，正确且尖锐的估计是
\[
\boxed{|X|\le |d\sigma|\,Q\sqrt e}.
\]
相应 Young 估计为
\[
\boxed{
3X\ge-\frac92\eta |d\sigma|^2e-\frac{Q^2}{2\eta}
\qquad(\eta>0),
}
\]
而不是余项 \(Q/(2\eta)\)。脚本的零残差仅验证了其输入的代数 Young 恒等式，并未验证错误的几何幅值。

## 3. 混合 Ricci 缺陷与 \(dq\) 的精确系数

令
\[
\mathcal E_{ia}:=E(e_i^H,K_a),\qquad E=\operatorname{Ric}_g+3g,
\]
其中第二指标使用基本垂直场 \(K_a\)。与 Step 89 的显式混合 Ricci 公式相配的 Maxwell 方程为（基底定向可改变星号整体符号）
\[
\boxed{dq_a=2\rho\, *_\gamma\mathcal E_a}.
\]
例如 Step 89 的坐标公式确实给出
\[
\partial_zq_1=2\rho\,\operatorname{Ric}(e_r,K_1)
\]
（正负取决于 \( *_\gamma\) 约定）。

若单个水平—垂直块的 Hilbert–Schmidt 范数定义为
\[
|\mathcal E|^2
=\gamma^{ij}G^{ab}\mathcal E_{ia}\mathcal E_{jb},
\]
则因 \(G^{-1}=\rho^{-1}M^{-1}\)，有精确不变量关系
\[
\boxed{|b|^2=4|\mathcal E|^2}.
\]
注意完整对称二阶张量范数会把两个转置混合块都计入，故混合部分贡献 \(2|\mathcal E|^2\)。

若 \(\|E\|_{\mathrm{op}}\le\delta\)，该 \(2\times2\) 混合块满足
\[
|\mathcal E|_{\rm HS}\le\sqrt2\,\delta,
\]
因而
\[
\boxed{|b|\le2\sqrt2\,\delta}.
\]
`step90_charge_potential_verify.py` 中所谓 Maxwell norm residual 本身只是恒等式占位符；真正的系数核验来自上述混合 Ricci 坐标公式及指标换算。

## 4. 圆 cusp 上的物理 Maxwell 定律

在对角电荷取向下定义
\[
w=e^{-(3\sigma+\alpha)/2}q_1,\qquad
b_r=e^{-(3\sigma+\alpha)/2}q_1'.
\]
直接微分得到
\[
\boxed{
w'+\left(\frac32\sigma'+\frac12\alpha'\right)w=b_r.
}
\]
圆形向外扩张 cusp 上 \(\sigma=2r,\alpha=0\)，故
\[
\boxed{w'+3w=b_r}.
\]
若 \(|b_r|\le B\)，则
\[
|w(r)|\le e^{-3(r-r_0)}|w(r_0)|
+\frac B3\bigl(1-e^{-3(r-r_0)}\bigr).
\]
因此持续的混合 Ricci 强迫允许 \(w=O(B)\)；它不强迫 \(w\to0\)。只有 \(b_r=0\) 时才得到 \(e^{-3r}\) 衰减。

## 5. 精确结构化 Bochner 恒等式与 \(+Qe\) 消去

将垂直无迹缺陷写成
\[
Z=-2\widehat E_0,\qquad
\tau_\sigma(U)=S_F+Z=-\nabla Q+Z,
\]
并令
\[
A=U^*h,\qquad y=dU(\nabla\sigma),\qquad
V_Z(X)=\langle dU(X),Z\rangle .
\]
水平约化方程是
\[
\operatorname{Ric}^4_\sigma
=(-3+Q)\gamma_B+\frac12A+E_B.
\]
于是
\[
\boxed{
\begin{aligned}
\frac12Le={}&|DdU|^2+\frac12e^2+\det A-3e+E_B{:}A\\
&+\frac12|y|^2+3\langle y,\nabla Q\rangle+R_q\\
&+\operatorname{div}_\sigma V_Z
+\langle\nabla Q,Z\rangle-|Z|^2 .
\end{aligned}}
\]

这里答案明确为：

\[
\boxed{\text{水平漂移曲率中的 }+Qe\text{ 与 }DS_F\text{ 中的 }-Qe
\text{ 点态、精确地消去。}}
\]

该消去对变量 \(Q(x)\) 仍成立，无需 \(Q\) 常数。因此 Step 89 的“扭率给出有利的净 \(+Qe\) 反应”只适用于把整个扭率源留在散度中的另一种记账方式；完全展开后没有残留的 \(+Qe\) 基项。

保留平方配方可得
\[
\frac12|y|^2+3\langle y,\nabla Q\rangle
=\frac12|y+3\nabla Q|^2-\frac92Q^2.
\]
若 \(\|E\|_{\rm op}\le\delta\)，则
\[
|Z|\le2\delta,\qquad |V_Z|\le2\delta\sqrt e,
\]
从而目前最强的纯 \(e\) 结构化下界之一是
\[
\boxed{
\begin{aligned}
\frac12Le\ge{}&
|DdU|^2+\det A+\frac12e^2-(3+\delta)e
+\operatorname{div}_\sigma V_Z\\
&-\frac92Q^2-\sqrt{2Qe}\,|b|-2\delta Q-4\delta^2 .
\end{aligned}}
\]
例如
\[
\sqrt{2Qe}|b|
\le \eta e+\frac{Q|b|^2}{2\eta}
\le\eta e+\frac{4Q\delta^2}{\eta}.
\]
此式不把变量 \(Q\) 当常数，但仍需要控制 \(Q\)。

## 6. 另一种完整散度形式及可靠的变量-\(Q\) 上界

若不展开 \(S_F\)，令
\[
V(X)=\langle dU(X),\tau_\sigma(U)\rangle ,
\]
则等价地
\[
\frac12Le
=
|DdU|^2+\frac12|y|^2+\frac12e^2+\det A
-(3-Q)e+E_B{:}A
+\operatorname{div}_\sigma V-|\tau_\sigma(U)|^2.
\]

必须区分
\[
Q_-:=\inf_BQ,\qquad Q_+:=\sup_BQ,\qquad
Q_C:=\langle Q\rangle_C
\]
（最后一个是极小分隔曲线上的加权平均）。置
\[
K:=3-Q_-+\delta,\qquad f:=Q_++2\delta.
\]
则
\[
\boxed{
\frac12Le\ge\frac12e^2-Ke+\operatorname{div}_\sigma V-f^2,
\qquad |V|\le f\sqrt e .
}
\]
在 Step 87 相同的完备性、Green 核及无穷远通量假设下，若 \(K>0\)，取常质量 \(\kappa=2K\)，得到
\[
\boxed{
\sup_Be\le
\left[
\frac{2f}{\sqrt K}
+\sqrt{2K+\frac{5f^2}{K}}
\right]^2 .
}
\]
这没有把空间变量 \(Q\) 放入“变量质量 resolvent”；它只使用 \(\inf Q\) 和 \(\sup Q\) 的常数界。

若精确 OT 开端上 \(Q=0\)，则
\[
Q_-=0,\qquad K=3+\delta;
\]
此时扭率并不改善全局统一曲率参数。Step 89 的 \(Q_*\simeq0.8986\) 只属于额外假设 \(Q(x)\equiv q\) 的算术特例；电荷向量 \(q\) 常数并不推出
\[
Q=\tfrac12e^{-3\sigma}q^TM^{-1}q
\]
为空间常数。

## 7. 分隔面系数

对不变极小分隔面，
\[
\sum_A|\mathrm{II}(T,E_A)|^2=\frac Q2.
\]
由于完整对称张量范数同时计入 \((T,E_A)\) 与 \((E_A,T)\)，混合贡献为
\[
\boxed{|\mathrm{II}|^2_{\rm mixed}=Q}.
\]
故
\[
\boxed{\langle e_s\rangle_C\ge12+2Q_C-8\delta}.
\]
Step 89 若把“单个垂直指标求和”直接写成 \(Q\)，存在因子二的记号错误；但其最终 \(|\mathrm{II}|^2\ge Q\) 以及分隔面下界是正确的。

结合 resolvent 上界，必要条件为
\[
\boxed{
12+2Q_C-8\delta
\le
\left[
\frac{2(Q_++2\delta)}{\sqrt{3-Q_-+\delta}}
+
\sqrt{
2(3-Q_-+\delta)
+\frac{5(Q_++2\delta)^2}{3-Q_-+\delta}}
\right]^2 .
}
\]
这里 \(Q_-,Q_+,Q_C\) 不能合并为同一个“\(Q\)”。

## 8. 面积方程没有提供进一步的精确消去

垂直迹方程是
\[
\boxed{L\sigma=6+Q-T},
\qquad T=\operatorname{tr}_GE_{VV}.
\]
对
\[
x=|\nabla\sigma|^2,\qquad W=e+cx
\]
可将交换项转移到通量，得到粗但闭合的联合能量下界
\[
\boxed{
\frac12LW\ge
\frac{W^2}{2(1+c)}-KW
+\operatorname{div}_\sigma\mathcal J_c
-f^2-cf(6+f),
}
\]
其中
\[
\mathcal J_c=V+c(Q-T)\nabla\sigma,\qquad
|\mathcal J_c|\le f\sqrt{1+c}\sqrt W.
\]

但：

\[
\boxed{\text{面积方程不产生第二个类似 }(+Qe)+(-Qe)=0\text{ 的精确消去。}}
\]

若展开 \(dQ\)，面积 Bochner 只会把 \(3X\) 改为 \((3+c)X\)，而不是消掉它；散度写法只是把它转移到 \((Q-T)\nabla\sigma\) 通量。尝试加入 \(LQ\) 在 \(dq\neq0\) 时会产生 \(q\) 的二阶导数，而混合 Ricci 缺陷只控制 \(dq\)，故当前假设不足以支持该路线。

## 9. 强迫扭率阻碍尚缺的核心对象

完整 forced-twist 阻碍尚未闭合。精确缺口是：仅由
\[
\|E\|_{\rm op}\le\delta
\]
及端部条件推导出维数一致的 \(Q_+\)（并最好同时控制 \(Q_C\)）上界，或建立能够直接处理上述变量势和联合通量的 resolvent/谱估计。

现有混合方程只给
\[
|b|\le2\sqrt2\,\delta.
\]
圆 cusp 方程表明持续小强迫允许 \(w=O(\delta)\)，而长或复杂核心可以累积电荷变化；现有材料没有推出普适的 \(\sup Q\) 控制。结构化 Bochner 式把大扭率通量换成 \(Q^2\) 及 \(Q|d\sigma|\sqrt e\)，完整散度式则直接需要 \(Q_+\)：两者都未消除这一缺口。

精确 Einstein 情形 \(dq=0\)；若连通 free 区域含 \(F=0\) 的精确 OT 开集，则 \(q=0\) 并因守恒而处处为零，退化回无扭率结果。该论证不适用于 forced 情形，也不适用于仅渐近 OT 的端。

以上结论不外推到非 free-\(T^2\) 度量或一般四维流形。
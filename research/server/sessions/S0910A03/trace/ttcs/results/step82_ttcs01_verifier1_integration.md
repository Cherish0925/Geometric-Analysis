# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 82,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step82_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step82_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the physical Gaussian-slice balance derivation for the orthogonally transitive T^2-invariant metric and sharpen what it says about reversal of mean horizontal contraction. Use E=Ric_g+3g, q_r=e^{2a}dz^2+G_ab dx^a dx^b, rho=sqrt(det G), u=a_r, B=(1/2)G^{-1}G_r, v=tr B, B0=B-(v/2)I, dmu=e^a rho dz, V=int dmu, I=int u dmu, J=int v dmu. Check (i) J'=6V-int tr_orbit(E)dmu, (ii) I'=3V+int R(q_r)dmu-int E_zz dmu, including why the intrinsic orbit-Ricci trace integrates to zero, and (iii) after the Hamilton constraint, whether the defect term is 2E_rr-E_zz or tr_orbit(E)-E_rr. Derive the necessary inequality at the first return I=0 after I<0 under ||E||op<=delta, carefully treating covariance, differentiability, and signs. Then investigate whether the orbit-map energy identity, matrix equation, base constraints, or J/V evolution yields a nontrivial bound on 2Cov(u,v)+<v^2>/2-<|B0|^2> strong enough to prevent reversal, or whether the balances alone admit algebraically favorable slices. Give direct mathematics, state exact hypotheses, and distinguish slice compatibility from dynamic reachability. Check the session scripts/data rather than trusting their summaries.

## Integrated Scientific Memo

# Gaussian 切片平衡的独立核验

设
\[
g=dr^2+q_r,\qquad
q_r=e^{2a(r,z)}dz^2+G_{ab}(r,z)\,dx^a dx^b
\]
定义在 \(r\)-区间与闭的自由 \(T^2\)-切片上；\(z\) 为周期坐标，\(G\) 正定。令
\[
\rho=\sqrt{\det G},\quad u=a_r,\quad
B=\frac12G^{-1}G_r,\quad v=\operatorname{tr}B,\quad
B_0=B-\frac v2I,
\]
以及
\[
S=\operatorname{diag}(u,B),\qquad H=\operatorname{tr}S=u+v.
\]
以下 \(E_{rr},E_{zz}\) 均指正交标架分量，
\[
E=\operatorname{Ric}_g+3g,\qquad
E_{\rm orb}=\operatorname{tr}_{T^2}E.
\]
切片测度及积分量为
\[
d\mu=e^a\rho\,dz,\qquad
V=\int d\mu,\quad I=\int u\,d\mu,\quad J=\int v\,d\mu .
\]

由于
\[
(d\mu)_r=H\,d\mu,
\]
故
\[
V'=I+J,\qquad
I'=\int(u_r+Hu)\,d\mu,\qquad
J'=\int(v_r+Hv)\,d\mu.
\]

## 1. 两个基本平衡式

Gaussian 叶分解给出
\[
\operatorname{Ric}_g|_{Tq}
=\operatorname{Ric}(q)-S_r-HS,
\]
因而
\[
S_r+HS=\operatorname{Ric}(q)+3I-E_T.
\]
分别取轨道块迹和单位 \(z\)-方向分量：
\[
v_r+Hv=R_{\rm orb}^{q}+6-E_{\rm orb},
\]
\[
u_r+Hu=R_{zz}^{q}+3-E_{zz}.
\]

### 内禀轨道 Ricci 迹为何积分为零

取物理弧长 \(ds=e^a dz\)，并置
\[
A=\frac12G^{-1}G_s,\qquad
\theta=\operatorname{tr}A=\frac{\rho_s}{\rho}.
\]
对
\[
q=ds^2+G(s)
\]
且 \(T^2\) 轨道平坦，有
\[
R_{\rm orb}^{q}
=-\theta_s-\theta^2
=-\rho^{-1}\partial_s(\rho\theta).
\]
因此
\[
\int R_{\rm orb}^{q}\,d\mu
=-\int\partial_s(\rho\theta)\,ds=0.
\]
在 \(z\) 坐标中等价地，
\[
R_{\rm orb}^{q}
=-e^{-a}\rho^{-1}
\partial_z\!\left(\rho e^{-a}\partial_z\log\rho\right).
\]
这只依赖面积函数 \(\rho\)，不依赖 \(G/\rho\) 的 unimodular 形状，故结论不要求 \(G\) 对角化。

由此得到
\[
\boxed{J'=6V-\int E_{\rm orb}\,d\mu.}
\]
再利用
\[
R(q)=R_{zz}^{q}+R_{\rm orb}^{q},
\]
得到
\[
\boxed{I'=3V+\int R(q)\,d\mu-\int E_{zz}\,d\mu.}
\]

源脚本的直接有限差分确实验证了这两式：
\[
I'_{\rm FD}-I'_{\rm RHS}\simeq-1.45\times10^{-12},\qquad
J'_{\rm FD}-J'_{\rm RHS}\simeq6.50\times10^{-12}.
\]

## 2. Hamilton/Gauss 改写：正确缺陷是 \(E_{\rm orb}-E_{rr}\)

关键处在于 contracted Gauss 恒等式：
\[
R(q)=R_g-2\operatorname{Ric}_g(\partial_r,\partial_r)
     +H^2-|S|^2.
\]
因
\[
R_g=\operatorname{tr}_gE-12,\qquad
\operatorname{Ric}_{rr}=E_{rr}-3,
\]
故严格地
\[
\boxed{
R(q)=-6+H^2-|S|^2+\operatorname{tr}_gE-2E_{rr}.
}
\]
也就是
\[
R(q)
=-6+H^2-|S|^2+E_{zz}+E_{\rm orb}-E_{rr}.
\]

此外
\[
|S|^2=u^2+\operatorname{tr}(B^2)
=u^2+\frac12v^2+|B_0|^2,
\]
所以
\[
H^2-|S|^2
=2uv+\frac12v^2-|B_0|^2.
\]
代入 \(I'\) 平衡式，得到精确恒等式
\[
\boxed{
I'=\int\left[
-3+2uv+\frac12v^2-|B_0|^2
+E_{\rm orb}-E_{rr}
\right]d\mu.
}
\]

因此第三项的正确答案是
\[
\boxed{\operatorname{tr}_{\rm orbit}(E)-E_{rr},}
\]
而不是 \(2E_{rr}-E_{zz}\)。

两种表达式之差为
\[
(2E_{rr}-E_{zz})-(E_{\rm orb}-E_{rr})
=4E_{rr}-\operatorname{tr}_gE,
\]
一般不为零。

这也解释了源脚本的数据：

- 使用 \(E_{\rm orb}-E_{rr}\) 的 `rhsTurnProposed_if_constraint`
  为 \(0.06513607870995765\)，与直接 \(I'\) 完全吻合；
- 使用 \(2E_{rr}-E_{zz}\) 的结果为 \(-0.2993294913539239\)；
- 差值正是所记录的 Hamilton residual \(0.36446557006388164\)。

脚本中
\[
R(q)=-6+H^2-|S|^2+2E_{rr}
\]
是错误的离壳延拓；它仅在 \(E=0\) 时与正确式同时退化为 Einstein Hamilton 约束。相关 JSON 的“correct/proposed”标签和文字结论应当反转。

## 3. 首次回返的必要条件

定义加权平均与协方差
\[
\langle f\rangle=\frac1V\int f\,d\mu,\qquad
\operatorname{Cov}(u,v)
=\langle uv\rangle-\langle u\rangle\langle v\rangle.
\]

设 \(r_*\) 是从负值首次回返：
\[
I(r_*)=0,\qquad I(r)<0
\quad(r_*-\varepsilon<r<r_*).
\]
只需度量在 \(r\) 上足够光滑使 \(I\in C^1\)。于是
\[
I'(r_*)
=\lim_{h\downarrow0}
\frac{I(r_*)-I(r_*-h)}h\ge0.
\]
这里符号是非负，而不是非正。

在 \(r_*\) 上，
\[
\langle u\rangle=\frac IV=0,\qquad
\langle uv\rangle=\operatorname{Cov}(u,v).
\]
故
\[
0\le \frac{I'}V
=-3+2\operatorname{Cov}(u,v)
+\frac12\langle v^2\rangle
-\langle|B_0|^2\rangle
+\langle E_{\rm orb}-E_{rr}\rangle.
\]

若逐点
\[
\|E\|_{\mathrm{op}}\le\delta,
\]
其中算子范数相对于 \(g\)，则每个正交方向上的 Rayleigh 商绝对值不超过 \(\delta\)，从而
\[
E_{\rm orb}-E_{rr}\le
|E_x|+|E_y|+|E_{rr}|\le3\delta.
\]
因此首次回返必满足
\[
\boxed{
2\operatorname{Cov}(u,v)
+\frac12\langle v^2\rangle
-\langle|B_0|^2\rangle
\ge 3-3\delta.
}
\]

写 \(y=\langle v\rangle=J/V\)，则左边也可写为
\[
2\operatorname{Cov}(u,v)
+\frac12\operatorname{Var}(v)
+\frac12y^2
-\langle|B_0|^2\rangle.
\]
因此平均轨道膨胀、轨道膨胀的空间方差以及正的 \(u\)-\(v\) 协方差有利于回返；径向轨道剪切阻碍回返。

虽然源脚本用了错误的精确缺陷项，但粗阈值偶然不变，因为
\[
|E_{\rm orb}-E_{rr}|\le3\delta,\qquad
|2E_{rr}-E_{zz}|\le3\delta.
\]
任何利用缺陷方向结构的精细估计则必须采用正确组合。

## 4. 等价的切向轨道能量判据

写
\[
G=\rho M,\qquad \det M=1,
\]
令 \(U\) 为对应的
\(SL(2,\mathbb R)/SO(2)\) 轨道映射，并采用
\[
|U_s|^2=\frac12\operatorname{tr}
\bigl((M^{-1}M_s)^2\bigr).
\]
切片标量曲率为
\[
R(q)=-2\theta_s-\frac32\theta^2-\frac12|U_s|^2.
\]
用 \(\rho_s=\theta\rho\) 分部积分：
\[
\int -2\theta_s\,\rho ds
=2\int\theta^2\rho ds,
\]
故
\[
\boxed{
\langle R(q)\rangle
=\frac12\langle\theta^2-|U_s|^2\rangle.
}
\]
于是
\[
\frac{I'}V
=3+\frac12\langle\theta^2-|U_s|^2\rangle
-\langle E_{zz}\rangle.
\]
在回返点，
\[
\boxed{
\langle |U_s|^2-\theta^2\rangle
\le 6-2\langle E_{zz}\rangle
\le 6+2\delta.
}
\]

对精确反射中心 \(R(q_0)=-6\)，有
\[
\langle|U_s|^2-\theta^2\rangle_{r=0}=12,
\qquad I'(0)=-3V.
\]
所以后续回返至少要求该加权切向能量差从 \(12\) 降至不超过 \(6+2\delta\)。这是有内容的必要转变，但本身不是单调性定理。

## 5. 其余方程并未给出足以排除回返的切片估计

令
\[
x=\frac IV=\langle u\rangle,\qquad
y=\frac JV=\langle v\rangle.
\]
由 \(V'=I+J\) 和 \(J'\) 得
\[
\frac{V'}V=x+y,
\]
\[
\boxed{
y'=6-\langle E_{\rm orb}\rangle-y(x+y).
}
\]
在 \(x=0\) 的回返切片上，
\[
y'=6-\langle E_{\rm orb}\rangle-y^2.
\]
它仅控制均值 \(y\)，不控制
\[
\operatorname{Var}(v),\qquad
\operatorname{Cov}(u,v),\qquad
\langle|B_0|^2\rangle.
\]
若从反射中心 \(J(0)=0\) 出发且 \(\delta<3\)，则
\[
J'\ge(6-2\delta)V>0,
\]
故随后 \(y>0\)；这甚至有利于 \(y^2/2\) 项，而非排除回返。

完整轨道矩阵方程为
\[
\partial_r(e^a\rho P_r)
+\partial_z(e^{-a}\rho P_z)
=-2e^a\rho\,(E^\sharp_{\rm orb})_0,
\qquad P_i=M^{-1}M_i.
\]
精确 Einstein 且中心反射时，
\[
\int e^a\rho P_r\,dz=0.
\]
但矩阵平均为零不蕴含 \(L^2\) 小性；它容许大的振荡 \(P_r\)，所以不给出
\[
|B_0|^2=\frac14\operatorname{tr}(P_r^2)
\]
的有用上界。混合 base 约束同样是无定号的微分关系，现有形式不能把正协方差或 \(v\) 的方差压到阈值以下。

因此，轨道映射能量恒等式、矩阵 Noether 约束、base 约束以及 \(J/V\) 演化，按所给材料均不能推出
\[
2\operatorname{Cov}(u,v)
+\frac12\langle v^2\rangle
-\langle|B_0|^2\rangle<3-3\delta.
\]

## 6. 切片兼容性与动力学可达性

仅从矩量看，有大量有利切片。例如在归一化周期测度下取
\[
u=2\cos z,\qquad v=2\cos z,\qquad B_0=0,
\]
则
\[
2\operatorname{Cov}(u,v)
+\frac12\langle v^2\rangle=5.
\]
因此积分平衡本身不排除回返。不过该例没有施加 Hamilton、混合约束或 PDE 演化，故只是代数兼容。

更强的是存在局部精确 Einstein 回返 germ。取空间齐次各向同性轨道模型
\[
g=dr^2+e^{2a(r)}dz^2+e^{2b(r)}(dx^2+dy^2),
\qquad u=a',\quad p=b',\quad v=2p.
\]
切片内禀平坦，Einstein 切向方程为
\[
u'=3-u(u+2p),\qquad
p'=3-p(u+2p).
\]
在 \(r=0\) 取
\[
u(0)=0,\qquad p(0)=\sqrt3.
\]
则
\[
H^2-|S|^2=(2\sqrt3)^2-2(\sqrt3)^2=6,
\]
Hamilton 约束成立，混合约束恒为零；且
\[
u'(0)=3,\qquad I'(0)=3V>0.
\]
由于
\[
u(r)=3r+O(r^2),
\]
在足够小的负 \(r\) 上 \(I<0\)，故 \(r=0\) 是真正的局部精确回返。

这并不解决目标中心的可达性：该 germ 在回返点有 \(p\ne0\)，不是反射切片，也不是从反射的 \(R(q_0)=-6\) 中心构造出的全局连接。它只严格证明：Einstein 方程和全部局部约束并不普遍禁止水平平均收缩反转。

## 结论

核验结果为：

\[
\boxed{J'=6V-\int\operatorname{tr}_{\rm orbit}(E)\,d\mu,}
\]
\[
\boxed{I'=3V+\int R(q_r)\,d\mu-\int E_{zz}\,d\mu,}
\]
并且正确的 Hamilton 改写是
\[
\boxed{
I'=\int\left[
-3+2uv+\frac12v^2-|B_0|^2
+\operatorname{tr}_{\rm orbit}(E)-E_{rr}
\right]d\mu.
}
\]

首次从 \(I<0\) 回到 \(I=0\) 时，在
\(\|E\|_{\rm op}\le\delta\) 下必要有
\[
\boxed{
2\operatorname{Cov}(u,v)
+\frac12\langle v^2\rangle
-\langle|B_0|^2\rangle
\ge3-3\delta.
}
\]

现有平衡式和约束没有给出足以违反该条件的普适估计；它们允许代数上有利的切片，甚至允许局部精确 Einstein 回返 germ。精确未决对象是全局动力学可达性：从指定的反射 \(R=-6\) 中心出发，切向轨道能量差能否从 \(12\) 降至 \(6+O(\delta)\)，同时不产生足以压倒协方差和轨道面积方差的径向剪切。
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
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step82_ttcs02_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step82_ttcs02_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Resolve a possible error in the proposed radial production law for K in the Step-82 note. Work in fixed periodic z coordinates with physical arclength derivative D_s=e^{-a}∂_z, measure dμ=e^aρ dz=ρ ds, σ=logρ, h=D_sσ, U:S^1→H^2, A=D_sU, b=∂_rU, e=|A|^2, k=e-h^2, K=<k>, u=a_r, v=σ_r, H=u+v, x=<u>, y=<v>. Use only target covariant derivatives, [∂_r,D_s]=-uD_s, and normalized moving averages. Independently derive K'. Check whether the exact kinematic identity is K'=-2<τ,b>+2<vc>+Cov(v-u,k)-2xK with τ=∇_sA+hA and c=h_s+h^2, or whether an additional explicit traceless-orbit defect term belongs while τ is retained. Then derive the Codazzi relation with E=Ric+3g and all normalization factors. For exact reflected scalar-minus-six center, verify u_r=-k/4, v_r=3+k/4, b_r=-τ (under the chosen target normalization), K'(0)=0, and K''(0)=72+2<|τ|^2>+(3/8)Var(k). State precisely how orbit defect enters if one substitutes the orbit evolution for τ, and flag double counting. Also check the x cubic coefficient. Ground the answer in the actual Step-82 files, but recompute rather than trusting the prior generator.

## Integrated Scientific Memo

## Step-82 核验结论

在固定周期坐标 \(z\) 下令
\[
D_s=e^{-a}\partial_z,\qquad d\mu=e^a\rho\,dz=\rho\,ds,
\]
并用 \(\langle\cdot\rangle\) 表示关于 \(d\mu\) 的归一化平均。重新计算确认：

\[
\boxed{
K'=-2\langle \tau,b\rangle+2\langle vc\rangle
+\operatorname{Cov}(v-u,k)-2xK.}
\tag{1}
\]

这是纯运动学恒等式；保留
\[
\tau=\nabla_sA+hA
\]
时，**不得再加入显式 traceless-orbit defect 项**。因此 Step-82 的 (8.1) 中
\[
+2\langle\mathcal E_0,b\rangle
\]
应删除。它既重复使用了轨道演化方程，而且若约定
\[
\nabla_rb+Hb+\tau=\mathcal E_0,
\]
则消去 \(\tau\) 后缺陷项的符号应为负而不是正。

---

## 1. \(K'\) 的直接推导

移动测度满足
\[
(d\mu)_r=H\,d\mu,\qquad H=u+v,
\]
故
\[
\frac d{dr}\langle f\rangle
=\langle f_r\rangle+\operatorname{Cov}(H,f).
\tag{2}
\]

由
\[
[\partial_r,D_s]=-uD_s
\]
以及目标联络无挠，
\[
\nabla_rA=\nabla_sb-uA,\qquad h_r=D_sv-uh.
\tag{3}
\]
因此
\[
e_r=2\langle A,\nabla_sb\rangle_{\mathbb H^2}-2ue
\]
和
\[
k_r
=2\langle A,\nabla_sb\rangle_{\mathbb H^2}
-2hD_sv-2uk.
\tag{4}
\]

周期加权分部积分给出
\[
\left\langle\langle A,\nabla_sb\rangle_{\mathbb H^2}\right\rangle
=-\langle\langle\nabla_sA+hA,b\rangle_{\mathbb H^2}\rangle
=-\langle\tau,b\rangle,
\tag{5}
\]
以及
\[
\langle hD_sv\rangle
=-\langle v(h_s+h^2)\rangle=-\langle vc\rangle.
\tag{6}
\]
所以
\[
\langle k_r\rangle
=-2\langle\tau,b\rangle+2\langle vc\rangle-2\langle uk\rangle.
\tag{7}
\]
结合 (2)，
\[
\begin{aligned}
K'
&=-2\langle\tau,b\rangle+2\langle vc\rangle
-2\langle uk\rangle+\operatorname{Cov}(u+v,k)\\
&=-2\langle\tau,b\rangle+2\langle vc\rangle
+\operatorname{Cov}(v-u,k)-2xK,
\end{aligned}
\]
即 (1)。

---

## 2. 轨道缺陷的精确位置与避免重复计数

采用 Step-81/82 的目标归一化，将目标切向量 \(W\) 对应到 traceless orbit endomorphism
\[
L_W=\frac12M^{-1}dM(W),
\]
并取
\[
\langle W,Z\rangle_{\mathbb H^2}=2\operatorname{tr}(L_WL_Z).
\tag{8}
\]
于是
\[
B_0=L_b,\qquad |b|^2=2|B_0|^2.
\tag{9}
\]

若记
\[
\mathsf E_0=(E_{\rm orb}^{\sharp})_0,\qquad
\varepsilon=L^{-1}(\mathsf E_0),
\]
则 traceless orbit 方程是
\[
\boxed{\nabla_rb+Hb+\tau=-\varepsilon.}
\tag{10}
\]
等价地，若把方程右端定义为
\[
\nabla_rb+Hb+\tau=\mathcal E_0,
\]
则
\[
\mathcal E_0=-\varepsilon.
\tag{11}
\]

消去 \(\tau\) 后，
\[
-2\langle\tau,b\rangle
=\langle(|b|^2)_r\rangle
+2\langle H|b|^2\rangle
+2\langle\varepsilon,b\rangle,
\tag{12}
\]
其中
\[
2\langle\varepsilon,b\rangle_{\mathbb H^2}
=4\operatorname{tr}(\mathsf E_0B_0).
\tag{13}
\]
用 \(\mathcal E_0\) 约定则同一项写成
\[
-2\langle\mathcal E_0,b\rangle.
\tag{14}
\]

故只有两种等价记账方式：

1. 保留 \(-2\langle\tau,b\rangle\)，没有显式 orbit defect；
2. 用轨道方程消去 \(\tau\)，显式缺陷恰好出现一次。

同时保留 \(-2\langle\tau,b\rangle\) 并再加缺陷项属于双重计数。Step-82 (8.1) 的五项版本因此错误。

---

## 3. Codazzi 关系及归一化

令
\[
C=\frac12G^{-1}D_sG=\frac h2I+C_0,\qquad
B=\frac12G^{-1}G_r=\frac v2I+B_0.
\]
切片形算子的散度满足
\[
(\operatorname{div}_qS)_s=D_su+hu-\operatorname{tr}(CB).
\]
由 contracted Codazzi，
\[
\operatorname{Ric}_{rs}
=(\operatorname{div}_qS)_s-D_sH
=hu-\operatorname{tr}(CB)-D_sv.
\tag{15}
\]
由于 \(g_{rs}=0\)，
\[
E_{rs}=\operatorname{Ric}_{rs}.
\]
而目标归一化给出
\[
\operatorname{tr}(CB)
=\frac{hv}{2}+\operatorname{tr}(C_0B_0)
=\frac{hv}{2}+\frac12\langle A,b\rangle_{\mathbb H^2}.
\tag{16}
\]
因此
\[
\boxed{
D_sv=h\left(u-\frac v2\right)
-\frac12\langle A,b\rangle_{\mathbb H^2}-E_{rs}.}
\tag{17}
\]

进一步，由加权分部积分，
\[
\boxed{
2\langle vc\rangle
=-2\langle h^2u\rangle+\langle h^2v\rangle
+\langle h\langle A,b\rangle_{\mathbb H^2}\rangle
+2\langle hE_{rs}\rangle.}
\tag{18}
\]
这里同样只能选择 \(2\langle vc\rangle\) 或其 Codazzi 展开式，不能两者同时加入。

---

## 4. 精确反射、标量曲率 \(-6\) 的中心

反射中心满足
\[
u=v=b=H=0.
\tag{19}
\]
切片内禀曲率分量为
\[
R^q_{ss}=-h_s-\frac12(h^2+e)
=-c-\frac12k,
\qquad
R^q_{\rm orb}=-h_s-h^2=-c.
\tag{20}
\]
总标量曲率
\[
R(q)=-2c-\frac12k.
\]
由 \(R(q)=-6\)，得到逐点恒等式
\[
\boxed{4c+k=12,\qquad c=\frac{12-k}{4}.}
\tag{21}
\]
此外
\[
\langle c\rangle=\langle h_s+h^2\rangle=0,
\]
故
\[
\boxed{K(0)=\langle k\rangle=12.}
\tag{22}
\]

精确 Einstein 切向演化在中心给出
\[
u_r=R^q_{ss}+3,\qquad v_r=R^q_{\rm orb}+6,
\]
从而
\[
\boxed{
u_r(0)=-\frac{k}{4},\qquad
v_r(0)=3+\frac{k}{4}.}
\tag{23}
\]
由无缺陷轨道方程，
\[
\boxed{\nabla_rb(0)=-\tau;}
\tag{24}
\]
因 \(b(0)=0\)，这也可写作 \(b_r(0)=-\tau\)。

代入 (1)，中心所有项均消失，因此
\[
\boxed{K'(0)=0.}
\tag{25}
\]

---

## 5. \(K''(0)\)

对 (1) 在中心求导。因为 \(H(0)=0\)，此处没有额外移动测度贡献。

各项依次为
\[
\left[-2\langle\tau,b\rangle\right]'_0
=2\langle|\tau|^2\rangle,
\tag{26}
\]
\[
\left[2\langle vc\rangle\right]'_0
=2\left\langle
\left(3+\frac k4\right)\frac{12-k}{4}
\right\rangle
=18-\frac18\langle k^2\rangle,
\tag{27}
\]
\[
\left[\operatorname{Cov}(v-u,k)\right]'_0
=\frac12\operatorname{Var}(k),
\tag{28}
\]
以及由 \(x'(0)=\langle u_r\rangle=-3\)、\(K(0)=12\)，
\[
[-2xK]'_0=72.
\tag{29}
\]
求和得到
\[
\boxed{
K''(0)=72+2\langle|\tau|^2\rangle
+\frac38\operatorname{Var}(k).}
\tag{30}
\]
等价地，
\[
K''(0)=18+2\langle|\tau|^2\rangle+\frac38\langle k^2\rangle.
\tag{31}
\]
因此
\[
K''(0)\ge72.
\]
这确认了 Step-82 §7 及 `step82_center_jet_invariants.py/json` 的代数结果；脚本自身只验证了代数，而上述推导补足了其所假设的几何输入。

---

## 6. \(x\) 的三次项

精确 Einstein 情形有
\[
x'=3-\frac12K-x(x+y).
\tag{32}
\]
利用反射奇偶性写成
\[
K=12+\frac12K''(0)r^2+O(r^4),
\quad
x=-3r+Ar^3+O(r^5),
\quad
y=6r+O(r^3).
\]
由于
\[
x(x+y)=-9r^2+O(r^4),
\]
比较 (32) 的 \(r^2\) 系数得到
\[
\boxed{A=3-\frac1{12}K''(0).}
\tag{33}
\]
故完整三次展开是
\[
\boxed{
x(r)=-3r-
\left(
3+\frac16\langle|\tau|^2\rangle
+\frac1{32}\operatorname{Var}(k)
\right)r^3+O(r^5).}
\tag{34}
\]
特别地三次系数不大于 \(-3\)，所以 Step-82 的
\[
x(r)\le -3r-3r^3+O(r^5)
\]
正确。脚本中的一般表达式 `3-K2/12` 也正确。

该三次公式要求邻域内为精确 Einstein germ。若仅有 \(E(0)=0\)，而非 \(E\equiv0\)，则 \(\langle E_{zz}\rangle\) 的二阶径向 jet 会额外贡献于 \(A\)。

---

## 最终勘误

Step-82 中应将候选式 (8.1) 改为
\[
\boxed{
K'=-2\langle\tau,b\rangle+2\langle vc\rangle
+\operatorname{Cov}(v-u,k)-2xK.}
\]

删除原来的
\[
+2\langle\mathcal E_0,b\rangle.
\]
若需要显式展示 traceless-orbit defect，则必须先用轨道演化消去 \(\tau\)；按
\[
\nabla_rb+Hb+\tau=\mathcal E_0
\]
的约定，缺陷项为
\[
-2\langle\mathcal E_0,b\rangle,
\]
且只出现一次。Codazzi 式、中心 jet、\(K'(0)\)、\(K''(0)\) 和 \(x\) 的三次系数均核验无误。
# 05 详细推导：ALE、Eguchi–Hanson、轨形解消与局部构造

## 1. bare Ricci-flat core 为什么不够

目标 \(\mathrm{Ric}\approx\sigma g\)，\(\sigma=\pm1\)。若直接把 Ricci-flat \(k\) 缩成 \(a^2k\)，
\[
\mathrm{Ric}_{a^2k}=0,
\]
因此
\[
(a^2k)^{-1}(0-\sigma a^2k)=-\sigma I,
\]
operator norm 恒为 1。

所以“缩小 bubble 的体积”不能隐藏 \(C^0\) Ricci defect。

## 2. refined Calabi/MV scaling

\[
g_t=t h_t,\qquad h_t=g_{\rm cal}+th,
\]
\[
\mathrm{Ric}(h_t)=t\Lambda h_t+t\lambda o+R_t,\quad
|R_t|_{g_{\rm cal}}\le Ct^2\rho^2.
\]
则
\[
g_t^{-1}(\mathrm{Ric}(g_t)-\Lambda g_t)
=
\lambda h_t^{-1}o+t^{-1}h_t^{-1}R_t.
\]

余项是 \(O(t\rho^2)\)：
- fixed core：\(O(t)\)；
- transition \(\rho\sim t^{-1/4}\)：\(O(t^{1/2})\)。

但 \(\lambda\neq0\) 时第一项趋向
\[
\lambda g_{\rm cal}^{-1}o,
\]
保持 order one。

**结论**：Yau-type \(C^0\) pinching 需要每个 local first obstruction 消失，或 varying family 中其相对 amplitude 消失。多节点的积分 cancellation 不够。

## 3. first obstruction=0 仍不等于 exact Einstein

还可能有：
- higher obstruction；
- global matching obstruction；
- complement inverse failure；
- unrelated far-away Einstein metric。

因此“首障碍零、二阶障碍非零”只能作为 local branch obstruction；必须另有 global smooth-type no-Einstein mechanism。

## 4. EH curvature energy

Ricci-flat ALE 4-manifold：
\[
\frac1{8\pi^2}\int_X|Rm|^2
=
\chi(X)-\frac1{|\Gamma|}.
\]
EH：
\[
\chi=2,\quad |\Gamma|=2,
\]
所以
\[
\boxed{\int|Rm|^2=12\pi^2}.
\]

## 5. EH 全非恒定 angular modes

\[
k=A^{-1}d\rho^2+\frac{\rho^2}{4}
(\sigma_1^2+\sigma_2^2+A\sigma_3^2),
\quad A=1-\rho^{-4}.
\]

固定偶数 \(l\) 与 Hopf mode \(m\)：
\[
(pF')'-qF=0,
\]
\[
p=\rho^3A,\quad
q=l(l+2)\rho+4m^2\rho(A^{-1}-1).
\]

取 \(z=\rho^l\)，有
\[
Lz=
-l(l-2)\rho^{l-3}
-4m^2\rho^{l+1}(A^{-1}-1)\le0.
\]
Wronskian
\[
J=p(zF'-z'F)
\]
满足
\[
J'=-FLz\ge0,
\]
且 bolt regularity 给 \(J\to0\)。故
\[
(F/\rho^l)'\ge0,
\]
\[
\boxed{\frac{F(\rho)}{F(R)}
\le(\rho/R)^l\le(\rho/R)^2}.
\]

这统一控制所有非恒定 angular frequencies。

## 6. exact Einstein EH-like core

研究稿构造
\[
q_\Lambda=
\frac{dr^2}{F_\Lambda}
+\frac{r^2}{4}
(\sigma_1^2+\sigma_2^2+G_\Lambda\sigma_3^2),
\qquad
\mathrm{Ric}(q_\Lambda)=\Lambda q_\Lambda.
\]

意义：bare EH defect=1 不代表 corrected core 不可能。一个 \(O(t^2)\) relative metric correction 经 second derivatives 与 scaling 可产生 order-one Ricci correction。

## 7. log annulus 与“同 Ricci、不同 Weyl”

logarithmic interpolation 路线强调：
- Ricci 是 Riemann contraction；
- Weyl 可在 Ricci 近固定时承担很大变化；
- 纯 Ricci pinching 不应被误当 full curvature control。

这与 Min-Oo 额外 \(d^2\max|K|\) 条件的出现相呼应。

## 8. positive EH first obstruction

normalized \(\mathrm{Ric}=g\) 的 A1 desingularization 中，一阶障碍与 \(R_+\) block 退化相关：
\[
R_+v=0,\qquad \det R_+=0.
\]
但
\[
\det R_+=0\not\Rightarrow \text{Kähler--Einstein}.
\]

## 9. C0-safe projection bridge

希望构造 approximate cokernel \(\Phi_i\)：
\[
\int\langle \mathrm{Ric}(g_i)-g_i,\Phi_i\rangle
=
t_i\mathcal O(R_+)+o(t_i),
\]
\[
\|\Phi_i\|_1=O(t_i).
\]

则 \(C^0\) pinching 直接给左边 \(O(\delta_it_i)\)。

困难：
- EH tail \(\rho^{-4}\)；
- ADM mass=0；
- 普通 translation/rotation flux 可能失明；
- quadratic test field 的长 annulus \(L^1\) mass 可能发散。

## 10. multi-node chirality

product-orbifold 上 single-node first obstruction 可同时为零，信息转移到：
- self terms；
- Green second jets；
- scalar/gauge/conformal global modes；
- ALE kernel parameters；
- chirality/orientation；
- complement solution。

后期 leading same/mixed chirality 结果属于这一 reduced map 的有限阶数据，不是 global no-Einstein theorem。

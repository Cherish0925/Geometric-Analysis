# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 71,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step71_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step71_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

The active goal is Yau Problem 26, but this task concerns the current negative-branch graph-neck route. Read the Step 70 and Step 71 materials plus the Li–Liu source excerpts. Independently derive and check: (i) the correct weighted normal balance for E=Ric+3g in Gaussian gauge; (ii) whether a complete exact reflection-symmetric half-core with a flat T^3 Poincare-Einstein end is ruled out by doubling and Proposition 6.6 (Witten–Yau/Cai–Galloway), including the warped-product exception; (iii) a complementing, reflection-compatible boundary formulation for the five T^2-invariant metric components in Einstein–DeTurck/Bianchi gauge. Be explicit about parity at t=0, which central metric data may vary, what geometric and gauge data belong at t=R, and why a zero of the gauge-fixed equations is or is not automatically Einstein on a manifold with boundary. Correct any sign, normalization, or boundary-count errors; do not infer nonlinear existence.

## Integrated Scientific Memo

## 核验结论

### 1. Gaussian gauge 中的加权法向平衡

令
\[
g=dt^2+h_t,\qquad
S=\frac12h_t^{-1}\partial_t h_t,\qquad H=\operatorname{tr}S,
\]
且 \(t\) 指向膨胀端。Riccati 公式为
\[
\operatorname{Ric}(\partial_t,\partial_t)=-H'-|S|^2.
\]
对
\[
E=\operatorname{Ric}+3g,\qquad B=S-I,\qquad b=H-3,
\]
有
\[
E_{00}=3-H'-|S|^2,
\qquad |S|^2=3+2b+|B|^2,
\]
故正确的点态恒等式是
\[
\boxed{b'+2b+|B|^2=-E_{00}.}
\]
乘以 \(e^{2t}\) 并积分得到
\[
\boxed{
e^{2R}b(R)-b(0)+\int_0^R e^{2t}|B|^2\,dt
=-\int_0^R e^{2t}E_{00}\,dt.}
\tag{1}
\]

反射中心满足 \(S(0)=0\)，所以 \(b(0)=-3\)。若末端要求 \(H(R)=3\)，则
\[
\boxed{
3+\int_0^R e^{2t}|S-I|^2\,dt
=-\int_0^R e^{2t}E_{00}\,dt.}
\tag{2}
\]
因此补偿所需的是加权平均意义下的 **负** \(E_{00}\)。若
\(\|E\|_{\mathrm{op}}\le\delta\)，则
\[
\boxed{
\delta\ge
\frac{2\left(3+\int_0^R e^{2t}|S-I|^2dt\right)}
{e^{2R}-1}
\ge \frac6{e^{2R}-1},}
\]
从而
\[
R\ge \frac12\log\!\left(1+\frac6\delta\right).
\]
Step 72 的符号正确；Step 70 中把 \(E_{00}\) 积分项写成正号的那一行错误，尽管其最终长度下界仍正确。

当 \(E=0\) 时，
\[
\boxed{
3-H(t)=e^{-2t}\left(3+\int_0^t e^{2s}|S-I|^2\,ds\right)>0.}
\tag{3}
\]
这严格推出 \(H<3\) 和 \(3-H\ge3e^{-2t}\)，但**不能单独推出**
\(H\to3\)，更不能推出 \(3-H\sim3e^{-2t}\)。还需证明
\[
e^{-2t}\int_0^t e^{2s}|S-I|^2\,ds\longrightarrow0.
\]

另有两项应修正：

* Step 70 的各向同性检验不是完整 Einstein 解。若
  \(h_t=e^{2f(t)}h_{\rm flat}\)，法向与切向方程分别为
  \[
  f''+(f')^2=1,\qquad f''+3(f')^2=3,
  \]
  联立强迫 \((f')^2=1,\ f''=0\)，故不存在 \(f'(0)=0\) 的此类 Einstein 解。
* Li–Liu Type-I 方程是
  \[
  (e^v)_{\xi\xi}+\Delta_{T^2}v=0.
  \]
  若 \(v=v(\xi,\theta)\)，则为
  \[
  (e^v)_{\xi\xi}+v_{\theta\theta}=0,
  \]
  不是 \((e^v)_{\xi\xi}+(e^v)_{\theta\theta}=0\)。其主部
  \(e^vv_{\xi\xi}+v_{\theta\theta}\) 确为椭圆型。

若精确半核具有光滑 PE 展开
\[
g=dt^2+e^{2t}\bigl(g_0+e^{-2t}g_2+O(e^{-3t})\bigr),
\qquad g_2=-P_{g_0},
\]
则
\[
e^{2t}(H-3)\longrightarrow \frac14R_{g_0}.
\]
由 (1) 得
\[
\boxed{
\frac14R_{g_0}
=-3-\int_0^\infty e^{2s}|S-I|^2\,ds<-3.}
\tag{4}
\]
所以该中心归一化的无穷远代表满足 \(R_{g_0}<-12\)，平坦共形无穷远不可能出现。

---

### 2. doubling 与 Proposition 6.6 的排除

设存在完整精确半核：

* \(\operatorname{Ric}=-3g\)；
* 关于 \(t=0\) 光滑反射对称；
* \(t=0\) 为固定 \(T^3\)；
* 唯一外端是具有平坦 \(T^3\) 共形无穷远的 PE 端。

沿 \(t=0\) 反射加倍后，得到一个完整、连通的负 Einstein 流形，具有两个同构 PE 端。平坦 \(T^3\) 共形类的 Yamabe 常数为零，因此 Li–Liu Proposition 6.6 适用。其两个“一端”分支立即排除；剩余例外只能是
\[
\mathbb R\times N,\qquad
g=ds^2+e^{-2s}g_N,\qquad \operatorname{Ric}_{g_N}=0.
\tag{5}
\]

该例外不挽救反射核：

* \(s\to-\infty\) 是 PE 端；
* \(s\to+\infty\) 是塌缩 AH cusp，而不是第二个 PE 端；
* 其切片 shape operator 恒为 \(S=-I\)，不存在 totally geodesic 切片，也不存在把两个 PE 端互换的中心反射。

故
\[
\boxed{\text{完整、精确、反射对称且具有平坦 }T^3\text{ PE 外端的半核不存在。}}
\]

这里必须使用真正的光滑反射对称性。单独 \(S(0)=0\) 只匹配一阶法向 jet，不能自动保证任意光滑度量的偶延拓光滑；反射对称性则给出全部奇偶 jet。

Li–Liu 的例子并不矛盾：其端结构正是“一端 PE、一端 cusp”，且不具有上述中心反射。一般非平坦例子的共形无穷远 Yamabe 常数为负，Proposition 6.6 也不适用。

---

### 3. 五分量 Einstein–DeTurck/Bianchi 边值问题

考虑附加 \(x,y\) 反射对称和正交分裂后的五分量 ansatz
\[
g=A\,dt^2+2D\,dt\,d\theta+C\,d\theta^2
  +P\,dx^2+Q\,dy^2,
\tag{6}
\]
其中系数依赖 \((t,\theta)\)。无这些额外离散对称时，一般 \(T^2\)-不变度量有更多分量；参考度量和边界数据必须保留这些对称性，五分量截断才闭合。

定义
\[
W^\mu=g^{\alpha\beta}
\bigl(\Gamma(g)^\mu_{\alpha\beta}
-\Gamma(\bar g)^\mu_{\alpha\beta}\bigr).
\]
以此 \(W\) 约定，正确的椭圆 DeTurck 方程是
\[
\boxed{
\Phi_{\bar g}(g)
=\operatorname{Ric}_g+3g-\frac12\mathcal L_Wg=0.}
\tag{7}
\]
其主符号为
\[
-\frac12g^{\alpha\beta}\xi_\alpha\xi_\beta\,\mathrm{Id}.
\]
Step 71 脚本计算的是 \(+\frac12\mathcal L_Wg\)，该符号不消去 Ricci 的微分同胚主部；JSON 中残留的混合二阶项正显示了这一点。脚本应改成 `-1/2*LV`。此外其参考双曲度量 \(dt^2+e^{2t}g_{T^3}\) 并不关于 \(t=0\) 对称，实际反射问题须改用偶参考度量。

#### 中心面 \(t=0\)

反射
\[
(t,\theta,x,y)\mapsto(-t,\theta,x,y)
\]
要求
\[
A,C,P,Q\ \text{为偶函数},\qquad D\ \text{为奇函数}.
\]
因此中心面的五个条件是
\[
\boxed{
D=0,\qquad
\partial_tA=\partial_tC=\partial_tP=\partial_tQ=0.}
\tag{8}
\]
这是一个 Dirichlet 加四个 Neumann 条件，与五个 Laplace 型方程逐分量互补，并自动编码 totally geodesic 固定集。

中心诱导度量
\[
q=C(0,\theta)d\theta^2+P(0,\theta)dx^2+Q(0,\theta)dy^2
\]
的三个函数值应当是解的输出，可以变化；不能再把指定的 \(q_N\) 三个分量作为额外 Dirichlet 数据，否则中心面共有八个条件而过定。\(A(0,\theta)\) 是 lapse/gauge 数据，不属于 \(q\)；\(\partial_tD(0,\theta)\) 也未被奇偶性固定。

若最终解确为 Einstein，则 Gauss 方程和 \(S=0\) 自动给出
\[
R_q=R_g-2\operatorname{Ric}(\nu,\nu)=-12+6=-6;
\]
这不是应另加的边界条件。

#### 外面 \(t=R\)

一个几何且 gauge-compatible 的五条件组合是
\[
\boxed{
[\gamma]=[\gamma_*],\qquad
H=H_*,\qquad
W^t=0,\qquad W^\theta=0,}
\tag{9}
\]
其中
\[
\gamma=C\,d\theta^2+P\,dx^2+Q\,dy^2.
\]
计数为：

* \([\gamma]=[\gamma_*]\)：两个函数，例如
  \(\log(P/C),\log(Q/C)\)；
* \(H=H_*\)：一个几何标量；
* \(W^t=W^\theta=0\)：两个 gauge 标量；
* 在五分量对称类中 \(W^x=W^y\equiv0\)。

对截断的膨胀双曲端，可取
\[
[\gamma_*]=[\gamma_{\rm flat}],\qquad H_*=3.
\]
公共共形因子及第二基本形式的无迹部分仍是输出。若要求与某个指定 cusp 截面精确拼接，则须匹配完整诱导度量及完整第二基本形式；那是更强的 Cauchy 匹配，不等同于互补椭圆边界数据 (9)。

冻结主符号后，令
\[
(p,q,r,s,u)
=(h_{nn},h_{n\theta},h_{\theta\theta},h_{xx},h_{yy})
\]
并取衰减模 \(e^{-kx+i\xi\theta}\), \(k=|\xi|\)。(9) 的主部为
\[
r-s=0,\qquad r-u=0,
\]
\[
\frac12\partial_n(r+s+u)-\partial_\theta q=0,
\]
\[
-\frac12\partial_np+\frac12\partial_n(r+s+u)-\partial_\theta q=0,
\]
\[
-\partial_nq+\frac12\partial_\theta(p-r+s+u)=0.
\]
写 \(r=s=u=a\)，模方程依次给出
\[
-\frac32ka-i\xi q=0,\qquad
\frac12kp=0,\qquad
kq+\frac{i\xi}{2}(p+a)=0,
\]
故 \(p=a=q=0\)，所有振幅皆零；Lopatinski 条件成立。

相比之下：

* 五分量全 Dirichlet 本身互补，但既不指定 \(H\)，也不保证 \(W=0\)；
* 只固定三个切向 metric 分量再加两个 Bianchi 条件并不互补，存在非零衰减 gauge 模。

---

### 4. gauge-fixed 零点是否自动 Einstein

一般而言，有限边界流形上的
\[
\Phi_{\bar g}(g)=0
\]
**不自动**意味着 \(W=0\)。特别是纯 Dirichlet metric 数据不控制由一阶导数组成的 \(W|_{\partial M}\)。

对上述特定问题，参考度量与解均可由奇偶性反射到
\([-R,R]\times T^3\)，而 (9) 在两个外边界给出 \(W=0\)。由 contracted Bianchi identity，
\[
\nabla^i\nabla_iW_j+\operatorname{Ric}_{jk}W^k=0.
\]
结合
\[
\operatorname{Ric}=-3g+\operatorname{sym}\nabla W
\]
并令 \(\phi=|W|^2\)，得到
\[
\boxed{
\frac12\bigl(\Delta\phi+W\cdot\nabla\phi\bigr)
=|\nabla W|^2+3\phi.}
\tag{10}
\]
由于外边界上 \(\phi=0\)，最大值原理推出 \(W\equiv0\)，故该特定反射问题的光滑零点确实是 Einstein。

若只使用五分量 Dirichlet 边界条件，则没有 \(W|_{t=R}=0\)，上述结论不成立；必须另有 gauge 边界条件、适当边界符号，或在完整/无穷远情形中有足够衰减以消除边界项。

这些结果只核准了必要平衡、flat-PE 反射核的严格排除，以及一个互补的 gauge-fixed 边值结构；它们不证明线性化可逆，也不推出任何非线性解的存在。
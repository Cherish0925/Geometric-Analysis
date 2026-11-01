# TTCS Independent Branch Record

```json
{
  "step_id": 83,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step82_slice_balances_and_reversal_energy.md",
    "Sessions/S0910A03/trace/ttcs/results/step82_ttcs02_verifier1_integration.md",
    "Sessions/S0910A03/workspace/data/step83_integrating_factor.json"
  ]
}
```

## Task

Verify the following claim for the OT reflected-center K-production. The quantities are: g=dr²+q_r Gaussian, dμ=e^a ρ dz, x=⟨u⟩_μ, y=⟨v⟩_μ, K=⟨e-h²⟩_μ, μ(r)=exp(2∫₀ʳ x ds). The K-production equation is K'+2xK = Φ where Φ = -2⟨τ,b⟩ + 2⟨vc⟩ + Cov(v-u,k). Eliminating τ via the orbit equation ∇_r b + Hb + τ = -ε (traceless orbit defect |ε|≤Cδ) and expanding vc via Codazzi gives: Φ = [d/dr⟨|b|²⟩ + 2(x+y)⟨|b|²⟩ + Cov(H,|b|²)] + [⟨h²(v-2u)⟩] + [⟨h⟨A,b⟩_H²⟩] + [Cov(v-u,k)] + [2⟨ε,b⟩ + 2⟨hE_rs⟩]. CLAIM 1: The μ-weighted integral satisfies ∫₀ᴿ μ[d/dr⟨|b|²⟩ + 2(x+y)⟨|b|²⟩] dr = μ(R)⟨|b|²⟩(R) + ∫₀ᴿ 2yμ⟨|b|²⟩ dr, which is non-negative when y≥0 throughout [0,R]. The proof: μ'=2xμ, so d/dr(μf)=μ(f'+2xf); integrating gives ∫μ(f'+2xf)dr = [μf]₀ᴿ; the remaining 2yf term adds the second integral. CLAIM 2: The circle-geometry term ⟨h²(v-2u)⟩≥0 whenever v≥0 and u≤0 pointwise. CLAIM 3: Only Cov(v-u,k) and ⟨h⟨A,b⟩⟩ can be negative. For a connector that lowers K from 12 to ≤6+2δ, the integrating-factor equation K(R)=μ(R)⁻¹[12+∫₀ᴿ μΦ dr] requires ∫₀ᴿ μΦ dr ≤-6+2δ. Given the non-negative contributions, the covariance/tension terms must supply at least -18 units of μ-weighted production. Check every step: signs, the IBP identity, hypothesis validity (is y≥0 and u≤0 guaranteed before return?), whether Cov(H,|b|²) belongs with the positive or indefinite group, and whether the ≥-18 budget is correctly computed.

## Output

# OT 反射中心 \(K\)-production 核验备忘

令
\[
m(r):=\exp\!\left(2\int_0^r x(s)\,ds\right)
\]
以区别于切片测度 \(d\mu\)，并置
\[
w=|b|^2,\qquad f=\langle w\rangle .
\]

## 1. 消去 \(\tau\) 后的公式与符号

归一化移动平均满足
\[
f'=2\langle\nabla_rb,b\rangle+\operatorname{Cov}(H,w).
\]
由
\[
\nabla_rb+Hb+\tau=-\varepsilon
\]
得到
\[
\begin{aligned}
-2\langle\tau,b\rangle
&=2\langle\nabla_rb,b\rangle+2\langle H|b|^2\rangle
  +2\langle\varepsilon,b\rangle\\
&=f'+2(x+y)f+\operatorname{Cov}(H,w)
  +2\langle\varepsilon,b\rangle .
\end{aligned}
\tag{1}
\]
这里 \(\operatorname{Cov}(H,w)\) 的系数和正号均正确。

Step-82 的 Codazzi 展开为
\[
2\langle vc\rangle
=\langle h^2(v-2u)\rangle
+\langle h\langle A,b\rangle_{\mathbb H^2}\rangle
+2\langle hE_{rs}\rangle .
\tag{2}
\]
所以题中给出的完整 \(\Phi\) 展开式正确，前提是轨道缺陷采用题中固定的
\(\nabla_rb+Hb+\tau=-\varepsilon\) 约定。

## 2. 积分因子恒等式

由于 \(m'=2xm\)，
\[
\begin{aligned}
\int_0^R m\,[f'+2(x+y)f]\,dr
&=[mf]_0^R+2\int_0^R myf\,dr\\
&=m(R)f(R)-f(0)+2\int_0^R myf\,dr .
\end{aligned}
\tag{3}
\]
精确反射中心有 \(b(0)=0\)，故 \(f(0)=0\)。因此题中的等式成立：
\[
\boxed{
\int_0^R m\,[f'+2(x+y)f]\,dr
=m(R)f(R)+2\int_0^R myf\,dr.}
\]
若 \(y\ge0\)，右端确实 \(\ge0\)。

不过，完整轨道项还含
\[
\int_0^R m\,\operatorname{Cov}(H,w)\,dr.
\]
该协方差符号不定。因此 (3) 只说明轨道项中去掉协方差后的部分非负，不能说明整个轨道项非负。

## 3. \(y\)、\(u\)、\(v\) 的符号假设

Step-82 的平均轨道方程是
\[
y'=6-\langle E_{\rm orb}\rangle-y(x+y),\qquad y(0)=0.
\tag{4}
\]
若 \(\|E\|_{\rm op}\le\delta<3\)，则
\[
|\langle E_{\rm orb}\rangle|\le2\delta,\qquad
6-\langle E_{\rm orb}\rangle\ge6-2\delta>0.
\]
因此 \(y\) 不能从零穿入 \(y<0\)，从而反射中心向外的区间上 \(y\ge0\)。精确 Einstein 情形当然也成立。若只有 traceless 缺陷 \(\varepsilon\) 的估计而没有 \(E_{\rm orb}\) 的估计，则不能仅据此推出 \(y\ge0\)。

另一方面，首次平均回返前只有
\[
x=\langle u\rangle<0,
\]
这并不推出 \(u\le0\) 逐点成立，也不推出 \(v\ge0\) 逐点成立。中心 jet 已直接显示这一点：
\[
u_r(0,z)=-\frac{k(z)}4,\qquad
v_r(0,z)=3+\frac{k(z)}4,
\qquad \langle k\rangle=12.
\]
\(\langle k\rangle=12\) 没有固定 \(k(z)\) 的逐点符号；例如 \(k(z)<0\) 的位置上，初始 \(u_r>0\)。

所以
\[
\langle h^2(v-2u)\rangle\ge0
\]
在逐点假设 \(v\ge0,\ u\le0\) 下代数上正确，但这些逐点假设并未由“首次平均回返前”推出。事实上
\[
\langle h^2(v-2u)\rangle
=\langle h^2\rangle (y-2x)
+\operatorname{Cov}(h^2,v-2u),
\tag{5}
\]
即使 \(y\ge0,x\le0\)，第二项仍可取任一符号。

## 4. 实际符号结构

在现有假设下：

- \(m(R)f(R)+2\int myf\ge0\)，若 \(y\ge0\)；
- \(\operatorname{Cov}(H,|b|^2)\) 符号不定；
- \(\langle h^2(v-2u)\rangle\) 在缺少逐点符号信息时符号不定；
- \(\langle h\langle A,b\rangle\rangle\) 符号不定；
- \(\operatorname{Cov}(v-u,k)\) 符号不定；
- \(2\langle\varepsilon,b\rangle+2\langle hE_{rs}\rangle\) 符号不定。

缺陷项虽有
\[
\left|2\langle\varepsilon,b\rangle
 +2\langle hE_{rs}\rangle\right|
\le
2C\delta\,f^{1/2}
+2\delta\,\langle h^2\rangle^{1/2},
\tag{6}
\]
但若 \(f\) 或 \(\langle h^2\rangle\) 很大，它仍可能贡献 \(O(1)\) 的下降量。

因此“只有 \(\operatorname{Cov}(v-u,k)\) 和 tension 项能向下贡献”并不成立。至少还包括
\(\operatorname{Cov}(H,|b|^2)\)、可能的 circle 项以及两个缺陷配对。

## 5. 正确的生产预算

积分因子方程精确给出
\[
\int_0^R m\Phi\,dr=m(R)K(R)-12.
\tag{7}
\]
若
\[
K(R)\le L:=6+2\delta,
\]
则
\[
\boxed{
\int_0^R m\Phi\,dr
\le m(R)(6+2\delta)-12.}
\tag{8}
\]
若 \(R\) 位于首次回返处或此前，则 \(x\le0\)，故 \(m(R)\le1\)，于是可进一步写成
\[
\int_0^R m\Phi\,dr\le-6+2\delta.
\tag{9}
\]
若 \(R\) 已越过首次回返，(9) 不再仅由现有信息推出，(8) 才是普遍适用的表达式。

定义已知非负的轨道部分
\[
P_{\rm orb}
=m(R)f(R)+2\int_0^R myf\,dr.
\]
其余项的积分 \(N\) 必须满足
\[
\boxed{
N\le m(R)(6+2\delta)-12-P_{\rm orb}.}
\tag{10}
\]
仅由 \(P_{\rm orb}\ge0\)，至多得到回返前
\[
N\le-6+2\delta,
\]
并不能得到 \(N\le-18\)。若另有独立估计 \(P_{\rm orb}\ge12\)，才可由粗略式 (9) 推出
\[
N\le-18+2\delta.
\]
目前材料中没有这样的统一下界。

中心 jet 也说明不存在固定的“初期正生产至少 \(12\)”：
\[
m(r)K(r)-12
=
\left(
\langle|\tau|^2\rangle
+\frac{3}{16}\operatorname{Var}(k)
\right)r^2+O(r^4),
\tag{11}
\]
其二次系数可以为零。`step83_integrating_factor.json` 中的 \(6.3316\) 来自所选
\(\langle|\tau|^2\rangle=16\) 模型，不是所有反射中心共有的下界。该文件还记录了积分因子误差 \(0.69688\) 和轨道恒等式差异 \(0.02865\)，因此这些数值不能建立精确的 \(18\)-单位预算。

综上：积分分部公式及其局部非负部分正确；circle 项的条件式正确但逐点条件未获保证；\(\operatorname{Cov}(H,|b|^2)\) 应归入符号不定部分；一般所需下降预算由 (8)–(10) 给出，而 \(18\) 需要额外的定量下界。
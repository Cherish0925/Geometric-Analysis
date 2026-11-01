# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 83,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step83_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step83_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the following claim for the OT reflected-center K-production. The quantities are: g=dr²+q_r Gaussian, dμ=e^a ρ dz, x=⟨u⟩_μ, y=⟨v⟩_μ, K=⟨e-h²⟩_μ, μ(r)=exp(2∫₀ʳ x ds). The K-production equation is K'+2xK = Φ where Φ = -2⟨τ,b⟩ + 2⟨vc⟩ + Cov(v-u,k). Eliminating τ via the orbit equation ∇_r b + Hb + τ = -ε (traceless orbit defect |ε|≤Cδ) and expanding vc via Codazzi gives: Φ = [d/dr⟨|b|²⟩ + 2(x+y)⟨|b|²⟩ + Cov(H,|b|²)] + [⟨h²(v-2u)⟩] + [⟨h⟨A,b⟩_H²⟩] + [Cov(v-u,k)] + [2⟨ε,b⟩ + 2⟨hE_rs⟩]. CLAIM 1: The μ-weighted integral satisfies ∫₀ᴿ μ[d/dr⟨|b|²⟩ + 2(x+y)⟨|b|²⟩] dr = μ(R)⟨|b|²⟩(R) + ∫₀ᴿ 2yμ⟨|b|²⟩ dr, which is non-negative when y≥0 throughout [0,R]. The proof: μ'=2xμ, so d/dr(μf)=μ(f'+2xf); integrating gives ∫μ(f'+2xf)dr = [μf]₀ᴿ; the remaining 2yf term adds the second integral. CLAIM 2: The circle-geometry term ⟨h²(v-2u)⟩≥0 whenever v≥0 and u≤0 pointwise. CLAIM 3: Only Cov(v-u,k) and ⟨h⟨A,b⟩⟩ can be negative. For a connector that lowers K from 12 to ≤6+2δ, the integrating-factor equation K(R)=μ(R)⁻¹[12+∫₀ᴿ μΦ dr] requires ∫₀ᴿ μΦ dr ≤-6+2δ. Given the non-negative contributions, the covariance/tension terms must supply at least -18 units of μ-weighted production. Check every step: signs, the IBP identity, hypothesis validity (is y≥0 and u≤0 guaranteed before return?), whether Cov(H,|b|²) belongs with the positive or indefinite group, and whether the ≥-18 budget is correctly computed.

## Integrated Scientific Memo

## 核验结论

为避免与切片测度 \(d\mu\) 混淆，记积分因子为
\[
m(r):=\exp\!\left(2\int_0^r x(s)\,ds\right),\qquad
f(r):=\langle |b|^2\rangle .
\]

题设消去 \(\tau\) 后的展开式符号正确：
\[
\begin{aligned}
\Phi={}&f'+2(x+y)f+\operatorname{Cov}(H,|b|^2)
+\langle h^2(v-2u)\rangle\\
&+\langle h\langle A,b\rangle_{\mathbb H^2}\rangle
+\operatorname{Cov}(v-u,k)
+2\langle\varepsilon,b\rangle+2\langle hE_{rs}\rangle .
\end{aligned}
\tag{1}
\]
但其符号分类和“至少 \(-18\)”的预算不成立。

### 1. 消去 \(\tau\) 的符号

由
\[
\nabla_rb+Hb+\tau=-\varepsilon
\]
以及移动平均公式
\[
f'=2\langle\nabla_rb,b\rangle+\operatorname{Cov}(H,|b|^2)
\]
可得
\[
\boxed{
-2\langle\tau,b\rangle
=f'+2(x+y)f+\operatorname{Cov}(H,|b|^2)
+2\langle\varepsilon,b\rangle .}
\tag{2}
\]
因此 \(\operatorname{Cov}(H,|b|^2)\) 的符号和系数 \(+1\) 都正确。缺陷项 \(2\langle\varepsilon,b\rangle\) 也符合题设的 \(-\varepsilon\) 约定。

Codazzi 展开同样正确：
\[
\boxed{
2\langle vc\rangle
=\langle h^2(v-2u)\rangle
+\langle h\langle A,b\rangle_{\mathbb H^2}\rangle
+2\langle hE_{rs}\rangle .}
\tag{3}
\]

### 2. Claim 1：IBP 恒等式正确，但需保留初端项

因为 \(m'=2xm\)，
\[
m\big(f'+2(x+y)f\big)=(mf)'+2myf.
\]
所以一般地
\[
\boxed{
\int_0^R m\big(f'+2(x+y)f\big)\,dr
=m(R)f(R)-f(0)+2\int_0^R myf\,dr .}
\tag{4}
\]
精确反射中心有 \(b(0)=0\)，故 \(f(0)=0\)，题中公式成立。若 \(y\ge0\) 于整个区间，则右端非负。

不过，这只控制 (1) 中的前两项；它**不包括**
\[
\operatorname{Cov}(H,|b|^2),
\]
后者符号不定。因此不能把完整的“orbit contribution”称为非负。

关于 \(y\ge0\)：现有完整缺陷控制下，它事实上可由平均方程推出，而不仅是中心附近成立。由
\[
y'=6-\langle E_{\rm orb}\rangle-y(x+y),\qquad y(0)=0,
\tag{5}
\]
若 \(\|E\|_{\rm op}\le\delta<3\)，则
\[
6-\langle E_{\rm orb}\rangle\ge 6-2\delta>0.
\]
若 \(y\) 试图首次穿过零进入负值，则在该零点有 \(y'>0\)，矛盾。因此
\[
\boxed{y(r)\ge0}
\]
在从反射中心向外的存在区间上成立。若只控制 traceless 缺陷 \(\varepsilon\)，而不控制 \(E_{\rm orb}\)，则不能作此结论。

### 3. Claim 2：条件式正确，但条件并未由“回返前”保证

若逐点
\[
v\ge0,\qquad u\le0,
\]
则 \(h^2(v-2u)\ge0\)，故
\[
\langle h^2(v-2u)\rangle\ge0.
\]
这一代数判断正确。

然而首次平均回返前只知道
\[
x=\langle u\rangle<0,
\]
而由上面至多得到 \(y=\langle v\rangle\ge0\)；这不推出逐点 \(u\le0\) 或 \(v\ge0\)。中心 jet 已显示
\[
u_r(0,z)=-\frac{k(z)}4,\qquad
v_r(0,z)=3+\frac{k(z)}4,\qquad \langle k\rangle=12,
\]
而 \(\langle k\rangle=12\) 不限制 \(k(z)\) 的逐点范围。例如 \(k(z)<0\) 处初始即有 \(u_r>0\)。

等价地，
\[
\langle h^2(v-2u)\rangle
=\langle h^2\rangle(y-2x)
+\operatorname{Cov}(h^2,v-2u),
\tag{6}
\]
即使 \(x\le0,y\ge0\)，协方差仍可使该项为负。

### 4. Claim 3 错误：所有符号不定项

在现有假设下，只有
\[
P_{\rm orb}:=m(R)f(R)+2\int_0^R myf\,dr
\tag{7}
\]
在 \(y\ge0\) 时确定非负。以下各项均可能负：

\[
\operatorname{Cov}(H,|b|^2),
\]
\[
\langle h^2(v-2u)\rangle
\quad\text{（除非另证逐点符号）},
\]
\[
\langle h\langle A,b\rangle_{\mathbb H^2}\rangle,
\qquad
\operatorname{Cov}(v-u,k),
\]
以及
\[
2\langle\varepsilon,b\rangle+2\langle hE_{rs}\rangle .
\]

缺陷配对虽满足类似
\[
\left|2\langle\varepsilon,b\rangle
+2\langle hE_{rs}\rangle\right|
\le
2C\delta\, f^{1/2}
+2\delta\,\langle h^2\rangle^{1/2},
\tag{8}
\]
但在 \(f\) 或 \(\langle h^2\rangle\) 很大时不必很小。

因此“只有 \(\operatorname{Cov}(v-u,k)\) 和 tension 项能为负”不成立。

### 5. 正确的 endpoint 预算

积分因子方程精确给出
\[
(mK)'=m\Phi,\qquad
\boxed{\int_0^R m\Phi\,dr=m(R)K(R)-12.}
\tag{9}
\]
若 \(K(R)\le6+2\delta\)，则
\[
\boxed{
\int_0^R m\Phi\,dr
\le m(R)(6+2\delta)-12.}
\tag{10}
\]
若 \(R\) 在首次 \(x=0\) 回返处或此前，则 \(x\le0\)，从而 \(m(R)\le1\)，故
\[
\boxed{
\int_0^R m\Phi\,dr\le -6+2\delta.}
\tag{11}
\]
这是正确但较弱的必要条件；精确界仍是 (10)。

把已证非负部分 \(P_{\rm orb}\) 分离，并令 \(N\) 为 (1) 中其余全部项的加权积分，则
\[
\boxed{
N\le m(R)(6+2\delta)-12-P_{\rm orb}.}
\tag{12}
\]
仅由 \(P_{\rm orb}\ge0\)，回返前只能推出
\[
N\le-6+2\delta,
\]
不能推出 \(-18\)。要得到
\[
N\le-18+2\delta,
\]
还必须另证 \(P_{\rm orb}\ge12\)；现有材料没有这一统一下界。

若考虑 \(m(R)\to0\) 的无限 expanding tail，(10) 会趋于 \(-12\)，但再减去所谓“早期 \(+6\)”仍需要一个可靠的早期正生产下界。中心展开
\[
m(r)K(r)-12
=
\left(
\langle|\tau|^2\rangle+\frac{3}{16}\operatorname{Var}(k)
\right)r^2+O(r^4)
\tag{13}
\]
的二次系数可以为零，因此不存在由 universal jet 单独给出的固定 \(+6\) 或 \(+12\) 下界。

此外，`step83_integrating_factor.json` 的 \(6.3316\) 是特定模型数值，不是定理；该文件自身报告
\[
\max |(mK)'-m\Phi|\approx0.697,
\]
所以不能以此建立精确的 \(-18\) 预算或 \(162.4\) 的强制负生产率。

## 最终判定

- **Claim 1：** 在反射中心 \(b(0)=0\) 且全程 \(y\ge0\) 时正确；但只证明两个指定项的积分非负，不包括 \(\operatorname{Cov}(H,|b|^2)\)。
- **Claim 2：** 条件命题正确；逐点 \(u\le0,v\ge0\) 并非首次平均回返前的已知结论。
- **Claim 3：** 错误。除所列两项外，\(\operatorname{Cov}(H,|b|^2)\)、circle 项和缺陷配对也都可能为负。
- **\(-18\) 预算：** 未被现有恒等式支持。一般正确预算是 (10)–(12)；回返前无额外下界时只能要求其余项合计至多 \(-6+2\delta\)。
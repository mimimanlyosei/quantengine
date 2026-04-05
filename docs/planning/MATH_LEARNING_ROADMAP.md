# QuantEngine Math Learning → Feature Roadmap

**Last updated:** April 5, 2026  
**Purpose:** Maps my math/quant learning curriculum to concrete features I'll build in QuantEngine. Each course leads to a buildable feature that demonstrates the concept in practice.

---

## Current Project State

- **v1.0:** ✅ Complete (compound growth calculator with auth, database, CRUD)
- **v2.0:** 🔄 In progress (refactor to modular architecture - Blueprints, testing, deployment)
- **v3.0:** 📋 Planned (F.I.R.E calculator - no advanced math required)
- **v4.0+:** 📋 Requires probability, statistics, time series knowledge

---

## Features I Can Build NOW (No New Math Needed)

### Investment Goal Calculator
**Math required:** Basic algebra (solving for variables)  
**What it does:** "I want £50,000 in 10 years. How much should I invest monthly?"  
**User inputs:** Target amount, years, expected return  
**Output:** Required monthly contribution  
**Why build it:** Practical feature, extends QuantEngine functionality

### Break-Even Calculator
**Math required:** Algebra (solving for time)  
**What it does:** "How long until my investment doubles?"  
**User inputs:** Initial investment, expected return  
**Output:** Years to double  
**Why build it:** Shows understanding of formula manipulation

### Inflation Adjuster
**Math required:** Compound growth (reverse direction)  
**What it does:** "What's my £50k worth in 20 years with 3% inflation?"  
**User inputs:** Future value, inflation rate, years  
**Output:** Real value (inflation-adjusted)  
**Why build it:** Demonstrates real-world financial concepts

---

## After Course 3: Probability Foundations → Monte Carlo Features (v4.0)

### What I'll Learn
- Probability distributions (normal, uniform)
- Expected value and variance
- Random sampling
- Probability of outcomes

### Feature 1: Basic Monte Carlo Simulator
**What it does:** "Run 1,000 simulations of your investment growing over 30 years"  
**User inputs:** Initial investment, expected return, volatility, years  
**Output:** Range of possible outcomes with probabilities  
**Example output:** "80% chance your £10k grows to between £40k-£80k"  
**Why build it:** Shows probabilistic thinking, not just single-point estimates

### Feature 2: Confidence Interval Display
**What it does:** Visual representation of "likely outcomes"  
**Output:** Chart showing 10th, 50th, 90th percentile outcomes  
**Example output:** "You have a 90% chance of ending up between £45k and £95k"  
**Why build it:** Makes uncertainty tangible for users

### Feature 3: Probability of Success Calculator
**What it does:** "What's the probability I reach my goal of £100k?"  
**User inputs:** Target amount  
**Output:** Percentage probability based on Monte Carlo runs  
**Example output:** "Based on 1,000 simulations, you have a 73% chance of reaching £100k"  
**Why build it:** Quantifies risk in user-friendly terms

---

## After Course 4: Statistics with Python → Risk Metrics (v4.0)

### What I'll Learn
- Standard deviation and variance
- Correlation
- Statistical significance
- Descriptive statistics

### Feature 1: Risk Score Calculator
**What it does:** Calculate standard deviation of returns  
**Output:** Risk rating (Low/Medium/High) based on volatility  
**Example output:** "Your portfolio has high volatility (±25% annual swing)"  
**Why build it:** Quantifies risk beyond just "optimistic/pessimistic"

### Feature 2: Sharpe Ratio
**What it does:** Risk-adjusted return metric  
**Formula:** (Return - Risk-Free Rate) / Standard Deviation  
**Output:** Single number showing return per unit of risk  
**Example output:** "Sharpe ratio of 1.5 means good risk-adjusted returns"  
**Why build it:** Professional metric investors actually use

### Feature 3: Maximum Drawdown
**What it does:** Worst peak-to-trough decline in simulation  
**Output:** "In worst case, your portfolio dropped 40% before recovering"  
**Why build it:** Shows users the downside risk

### Feature 4: Scenario Comparison Dashboard
**What it does:** Statistics across all saved scenarios  
**Output:** Average return, median years to goal, most common risk appetite  
**Why build it:** Uses descriptive statistics on user's own data

---

## After Course 5: Time Series & ARIMA → Backtesting (v4.0)

### What I'll Learn
- Time series analysis
- Trend detection
- Forecasting
- Historical data patterns

### Feature 1: Historical Backtest
**What it does:** "How would your strategy have performed from 2000-2020?"  
**User inputs:** Investment amount, monthly contribution  
**Data source:** Real S&P 500 historical returns  
**Output:** Actual vs predicted performance  
**Example output:** "Your £10k would have become £47k (model predicted £52k)"  
**Why build it:** Tests model against reality

### Feature 2: Best/Worst Historical Periods Analyzer
**What it does:** Identifies best and worst 10-year periods historically  
**Output:** "Best 10-year period: 1990-2000 (15% annual return)"  
**Output:** "Worst 10-year period: 2000-2010 (2% annual return)"  
**Why build it:** Shows users that timing matters

### Feature 3: Recovery Time Calculator
**What it does:** Based on historical crashes, how long to recover?  
**Example output:** "After 2008 crash, it took 5 years to recover"  
**Why build it:** Sets realistic expectations about volatility

---

## After Course 6: Intro to Quant Finance → Professional Features (v4.5)

### What I'll Learn
- Portfolio theory
- Asset allocation
- Risk management
- Financial instruments

### Feature 1: Asset Allocation Optimizer
**What it does:** Suggests mix of stocks/bonds based on risk tolerance  
**User inputs:** Age, risk appetite, years to retirement  
**Output:** "60% stocks, 40% bonds"  
**Why build it:** Practical financial advice

### Feature 2: Rebalancing Calculator
**What it does:** "When should you rebalance your portfolio?"  
**Output:** Notifications when allocation drifts >5% from target  
**Why build it:** Portfolio management feature

### Feature 3: Tax-Efficient Withdrawal Strategy
**What it does:** Optimize which accounts to withdraw from first  
**Why build it:** Real-world retirement planning

---

## After Courses 7-9: Advanced Math → Advanced Features (v5.0+)

### What I'll Learn
- Linear algebra (matrix operations, optimization)
- Multivariate calculus (gradients, optimization)
- Stochastic processes (random walks, Brownian motion)

### Feature 1: Portfolio Optimization
**What it does:** Find optimal asset weights using matrix math  
**Math:** Linear algebra for efficient frontier calculation  
**Why build it:** Classic quant finance problem

### Feature 2: Options Pricing Calculator
**What it does:** Price call/put options using Black-Scholes  
**Math:** Partial differential equations, stochastic calculus  
**Why build it:** Actual derivatives pricing

### Feature 3: Volatility Surface Visualizer
**What it does:** 3D visualization of option implied volatility  
**Math:** Multivariate calculus  
**Why build it:** Professional trading tool

---

## Learning Workflow: Course → Feature → Documentation → Portfolio

**For each course I complete:**

1. **Take the course** (Coursera/platform)
2. **Create GitHub issue** ("Add Monte Carlo simulation - #52")
3. **Build the feature** (apply the math concept in code)
4. **Write reflection** (`docs/learning/probability-reflection.md`)
5. **LinkedIn post** ("I just added Monte Carlo simulation to QuantEngine. Here's what I learned...")
6. **Update CV** (new feature = new demonstrated skill)

**This turns abstract math into portfolio-worthy projects.**

---

## Example: Probability Course → Monte Carlo Feature

**Week 1-4:** Take Probability Course
- Learn distributions, sampling, expected value

**Week 5:** Plan the Feature
- Create issue #52: "Add Monte Carlo simulation to QuantEngine"
- Define acceptance criteria (1,000 runs, show distribution, calculate probability of reaching goal)

**Week 6-7:** Build It
- Write `run_monte_carlo_simulation()` function
- Create route `/simulate`
- Add UI for inputting volatility
- Display results with chart

**Week 8:** Document & Share
- Write reflection connecting course concepts to code
- LinkedIn post with demo/screenshot
- Update CV: "Implemented Monte Carlo simulation for investment forecasting using probability theory and statistical sampling"

**Result:** Course certificate + working feature + LinkedIn proof + CV update

---

## Version Roadmap Timeline

### v2.0 (Now - May 2026)
- Modular architecture (Blueprints)
- Deployment to production
- Automated testing
- UI polish

### v3.0 (June-July 2026)
- F.I.R.E Calculator
- Investment Goal Calculator
- Break-Even Calculator
- Inflation Adjuster

### v4.0 (After Probability + Statistics Courses)
- Monte Carlo simulation
- Risk metrics (Sharpe, max drawdown)
- Historical backtesting
- Confidence intervals

### v4.5 (After Quant Finance Course)
- Asset allocation
- Rebalancing features
- Portfolio management tools

### v5.0+ (After Advanced Math Courses)
- Portfolio optimization
- Options pricing
- Advanced quant features

---

## Career Progression Roadmap

### Phase 1: Now - 2027 (Web Developer)
**Focus:** Get hired, build professional experience  
**Skills:** Flask, Django, Python, backend development, deployment  
**Projects:** QuantEngine (Flask), GridIQ (Django)  
**Salary:** £35-45k → £45-55k  
**Master's degree needed?** ❌ No

### Phase 2: 2027-2029 (Senior Web Dev or Data Engineer)
**Focus:** Technical depth, data-heavy projects  
**Skills:** Advanced backend, APIs, data engineering tools  
**Side learning:** Math courses (probability, statistics, time series)  
**Build:** Advanced QuantEngine features (Monte Carlo, risk metrics)  
**Salary:** £55-70k  
**Master's degree needed?** ❌ Still no

### Phase 3: 2029-2031 (Quantitative Developer OR Stay in Web/Data)
**Focus:** Financial applications, trading systems  
**Decision point:** Do I want quant research roles at top firms?  
**Skills:** Portfolio optimization, backtesting, financial modeling  
**Salary:** £70-100k+  
**Master's degree needed?** ⚠️ Only if targeting quant research at top firms (Two Sigma, Citadel, DE Shaw)

### Decision Point: 2029-2031
**By this time, I'll know:**
- What specific role I want
- Whether I need the credential
- If I can get company sponsorship
- If the ROI makes sense for a master's

**If pursuing quant research:** Consider part-time master's (company-sponsored)  
**If happy with quant dev or data engineering:** Master's not needed

---

## Master's Degree Assessment

### When a Master's Makes Sense
- ✅ I've worked as a developer for 2-3 years
- ✅ I've completed most of the self-learning math curriculum
- ✅ I know I want quant research roles (not just quant dev)
- ✅ I can afford it (time + money) or get company sponsorship
- ✅ I'm targeting top-tier quant firms that require advanced degrees

### When to Skip the Master's
- ❌ Haven't worked professionally yet (get experience first)
- ❌ Trying to "get foot in the door" (portfolio does this better)
- ❌ Not sure what I want (expensive way to figure it out)
- ❌ Think it's required for all quant work (it's not - only research roles)

### What Self-Learning Accomplishes
**Courses 1-6 give me:**
- ✅ Knowledge equivalent to ~60% of Financial Engineering master's
- ✅ Enough math for quant developer roles
- ✅ Portfolio features proving I understand concepts
- ✅ Cost: ~£500 for Coursera vs. £20-40k for master's

**What it doesn't give:**
- ❌ Credential/signal for top quant research firms
- ❌ Networking with quant students/professors
- ❌ Structured research projects

**Bottom line:** Don't need it for quant DEV. Only need it for quant RESEARCH at top firms.

---

## Key Principles

1. **Features make math real:** "I learned normal distributions" → "I used normal distributions to simulate 1,000 investment paths"
2. **Portfolio over credentials:** Hiring managers care what you've built, not what courses you've taken
3. **Ship before perfecting:** v1.0 deployed > v3.0 in progress
4. **Experience before education:** Get hired first, master's later if needed
5. **Build in public:** LinkedIn posts prove learning, create visibility

---

## Notes

- This roadmap is guidance, not a rigid plan
- Priorities may shift based on job market, opportunities, interests
- Each feature should be an independent GitHub issue
- Document learning reflections for future reference and LinkedIn content
- Focus on shipping working features, not perfect implementations

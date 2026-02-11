---
publish: 1
tags:
  - type/index
entity_extraction_done: true
---

See also: [[Runge-Kutta Yöntemleri (Sınav Odaklı Formüller)]], [[Numerical Differentiation]], [[Lagrange Interpolation]]

## overview: Bracketing Methods

Both the **Bisection Method** and the **Regula Falsi Method** are **bracketing methods** for finding the root of a continuous function $f(x)$.

**Core Principle:** They rely on the **Intermediate Value Theorem**.

1. Start with an interval $[a, b]$.
    
2. Ensure the function is continuous on this interval.
    
3. Check that $f(a)$ and $f(b)$ have **opposite signs**, meaning $f(a) \cdot f(b) < 0$.
    
4. If these conditions hold, there must be at least one root $p$ in the interval $(a, b)$ where $f(p) = 0$.
    

Both methods work by iteratively shrinking this bracket $[a, b]$ to converge on the root $p$. Their only difference is _how_ they choose the next test point $c$ within the interval.

---

## 1. Bisection Method (Interval Halving)

The Bisection Method is the simplest and most robust bracketing method. It finds the next test point by cutting the interval $[a, b]$ exactly in half.

### 🧠 Algorithm

1. **Initialize:** Find an interval $[a, b]$ such that $f(a) \cdot f(b) < 0$.
    
2. Iterate:
    
    a. Calculate the midpoint $c$:
    
    $$c = \frac{a+b}{2}$$
    
    b. Evaluate $f(c)$.
    
    c. Check for the new, smaller bracket:
    
    * If $f(a) \cdot f(c) < 0$, the root is in $[a, c]$. Set $b = c$.
    
    * If $f(c) \cdot f(b) < 0$, the root is in $[c, b]$. Set $a = c$.
    
    * If $f(c) = 0$, the root is $c$. (This is rare in practice).
    
3. **Terminate:** Repeat step 2 until the interval $[b-a]$ is smaller than a desired tolerance $\epsilon$.
    

### 📈 Convergence

- **Guaranteed:** Convergence is **always guaranteed** if the initial bracket is valid.
    
- **Rate:** The convergence is **linear** (Order of convergence $p=1$).
    
- **Speed:** It's very slow but predictable. The error is halved with each iteration. The error $E_n$ after $n$ iterations is $E_n = \frac{b-a}{2^n}$.
    

### ✅ Pros & Cons

- **Pro:** Extremely simple and robust. It **cannot fail** if started correctly.
    
- **Pro:** The number of iterations needed to achieve a specific tolerance can be calculated in advance.
    
- **Con:** **Very slow** convergence.
    
- **Con:** It completely ignores the _values_ of $f(a)$ and $f(b)$, only their signs. If $f(a)$ is much closer to zero than $f(b)$, the midpoint $c$ is not a very "smart" guess.
    

---

## 2. Regula Falsi (False Position Method)

The Regula Falsi Method tries to be "smarter" than Bisection. Instead of just taking the midpoint, it creates a **secant line** between $(a, f(a))$ and $(b, f(b))$ and estimates the root $c$ to be the **x-intercept** of this line.

### 🧠 Algorithm

1. **Initialize:** Find an interval $[a, b]$ such that $f(a) \cdot f(b) < 0$.
    
2. Iterate:
    
    a. Calculate the x-intercept $c$ of the secant line:
    
    $$c = \frac{a \cdot f(b) - b \cdot f(a)}{f(b) - f(a)}$$
    
    > Alternative Formula (easier to remember): $c = b - f(b) \cdot \frac{b-a}{f(b)-f(a)}$
    
    b. Evaluate $f(c)$.
    
    c. Check for the new, smaller bracket (same as Bisection):
    
    * If $f(a) \cdot f(c) < 0$, the root is in $[a, c]$. Set $b = c$.
    
    * If $f(c) \cdot f(b) < 0$, the root is in $[c, b]$. Set $a = c$.
    
3. **Terminate:** Repeat step 2 until the function value $|f(c)|$ is smaller than a desired tolerance $\epsilon$.
    

### 📈 Convergence

- **Guaranteed:** Convergence is also **always guaranteed**.
    
- **Rate:** The convergence is generally **superlinear** (faster than Bisection), but it can degrade to **linear** in the worst case.
    
- **The "Stuck Endpoint" Problem:** Regula Falsi's biggest weakness is that if the function is highly convex or concave in the bracket (e.g., $f(x) = x^2 - 2$ on $[0, 2]$), one of the endpoints (like $a$) might **get "stuck" and never move**. This causes the interval $[b-a]$ to converge to a non-zero width, and the method's convergence becomes slow (linear).
    

### ✅ Pros & Cons

- **Pro:** **Much faster** than Bisection in most typical cases. It uses the function values to make an intelligent guess.
    
- **Pro:** Retains the 100% convergence guarantee of the Bisection method.
    
- **Con:** Suffers from the "stuck endpoint" problem on one-sided, curved functions, making it converge very slowly (though it still converges).
    
- **Con:** The algorithm is slightly more complex to implement.
    

---

## 3. Comparison: Bisection vs. Regula Falsi

|**Feature**|**Bisection Method**|**Regula Falsi (False Position)**|
|---|---|---|
|**New Point $c$**|Midpoint of interval|x-intercept of secant line|
|**Formula for $c$**|$c = \frac{a+b}{2}$|$c = \frac{a f(b) - b f(a)}{f(b) - f(a)}$|
|**Convergence**|Guaranteed|Guaranteed|
|**Convergence Rate**|**Linear** ($p=1$)|**Superlinear** (typically), but can degrade to Linear|
|**Key Strength**|Absolute robustness, predictable error|Speed (usually)|
|**Key Weakness**|Always slow|Can become slow if one endpoint gets "stuck"|
|**Uses...**|Only the **signs** of $f(a), f(b)$|The **values** of $f(a), f(b)$|

Bkz: [[Matematik]] • [[Engineering]]


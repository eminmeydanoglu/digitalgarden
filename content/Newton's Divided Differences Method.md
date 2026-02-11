---
publish: 1
tags:
  - type/index
entity_extraction_done: true
---

[[Forward Divided Difference of Newton]]

The fundamental problem we're trying to solve is this:

> You are given a set of $n+1$ data points, $(x_0, y_0), (x_1, y_1), ..., (x_n, y_n)$. You assume these points come from some underlying function $f$, so $y_i = f(x_i)$. Your goal is to find a polynomial, $P_n(x)$, that passes _exactly_ through all these points.

Once you have this polynomial, you can use it to **interpolate**, or estimate the function's value at a new $x$ that is _between_ your known data points.

These slides present two ways to build this polynomial, both named after Newton.

---

### 1. Newton's Divided-Difference Method (The General Case)

This is the most general and robust of the two methods. It works whether your $x_i$ data points are spaced equally (like 1, 2, 3) or completely arbitrarily (like 1.0, 1.3, 1.6).

#### The "Newton Form" of the Polynomial

Instead of the standard $P_n(x) = c_0 + c_1x + c_2x^2 + ...$ form, Newton's method uses a cleverer, "nested" form:

$P_n(x) = a_0 + a_1(x-x_0) + a_2(x-x_0)(x-x_1) + ... + a_n(x-x_0)...(x-x_{n-1})$ 

The genius of this form is that the coefficients ($a_0, a_1, ...$) can be found one by one.

- To find $a_0$: We plug in $x = x_0$. All terms except the first one become zero.
    
    $P_n(x_0) = a_0$
    
    Since the polynomial must pass through $(x_0, f(x_0))$, we have our first coefficient:
    
    $a_0 = f(x_0)$ 
    
- To find $a_1$: We plug in $x = x_1$.
    
    $P_n(x_1) = a_0 + a_1(x_1-x_0)$
    
    We must have $P_n(x_1) = f(x_1)$, and we already know $a_0 = f(x_0)$.
    
    $f(x_1) = f(x_0) + a_1(x_1-x_0)$
    
    Rearranging to solve for $a_1$:
    
    $a_1 = \frac{f(x_1) - f(x_0)}{x_1 - x_0}$ 3
    

This pattern continues. Each new coefficient $a_k$ is found using the $k$-th data point, and it won't mess up the coefficients we've already found.

#### Divided-Difference Notation

These coefficients, $a_k$, are formally called **divided differences**. The notation looks recursive and is the key to calculating them efficiently4.

- Zeroth Divided Difference: This is just the function value itself.
    
    $f[x_i] = f(x_i)$ 5
    
- First Divided Difference: This is the slope between two points.
    
    $f[x_i, x_{i+1}] = \frac{f[x_{i+1}] - f[x_i]}{x_{i+1} - x_i}$ 6
    
- Second Divided Difference: This is the "slope of the slopes."
    
    $f[x_i, x_{i+1}, x_{i+2}] = \frac{f[x_{i+1}, x_{i+2}] - f[x_i, x_{i+1}]}{x_{i+2} - x_i}$ 7
    
- k-th Divided Difference (General Rule):
    
    $f[x_i, ..., x_{i+k}] = \frac{f[x_{i+1}, ..., x_{i+k}] - f[x_i, ..., x_{i+k-1}]}{x_{i+k} - x_i}$ 8
    
    (Notice the denominator always uses the outermost $x$-values).
    

With this notation, the coefficients for our polynomial are simply the divided differences that start with $x_0$:

$a_k = f[x_0, x_1, ..., x_k]$ 9

This gives us the final Newton's Divided-Difference Formula:

$$P_n(x) = f[x_0] + \sum_{k=1}^{n} \left( f[x_0, x_1, ..., x_k] \prod_{i=0}^{k-1} (x-x_i) \right)$$

(This is the formula written in summation form on the slide 10)

#### The Divided-Difference Table (Example 1)

This table 1111 is just a systematic way to calculate all the coefficients you need. The coefficients $a_k$ are **always the top diagonal** of this table.

Let's use the data from the slide 1212 to find $P_4(1.5)$.

|**xi​**|**f[xi​] (Col 1)**|**1st Div. Diff. (Col 2)**|**2nd Div. Diff. (Col 3)**|**3rd Div. Diff. (Col 4)**|**4th Div. Diff. (Col 5)**|
|---|---|---|---|---|---|
|**1.0**|**0.7681**|||||
|||**-0.4837**||||
|**1.3**|0.6200||**-0.1087**|||
|||-0.5489||**0.06587**||
|**1.6**|0.4554||-0.0494||**0.00182**|
|||-0.5786||0.06806||
|**1.9**|0.2818||-0.01187|||
|||-0.5715||||
|**2.2**|0.1103|||||

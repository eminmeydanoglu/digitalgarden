---
publish: 1
tags:
  - type/index
entity_extraction_done: true
---


### The Goal: A More "Snug" Fit

With [[Lagrange Interpolation]] , we found a polynomial $P_n(x)$ that matched $n+1$ function values $f(x_i)$.

With Hermite, we want a polynomial $H(x)$ that matches **both** the function value $f(x_i)$ and the derivative value $f'(x_i)$ at all $n+1$ points.

- **Given:** We have $n+1$ nodes ($x_0, \dots, x_n$).
    
- **Conditions:** For each node $x_i$, we have two conditions:
    
    1. $H(x_i) = f(x_i)$
        
    2. $H'(x_i) = f'(x_i)$
        
- **Total Conditions:** This gives us $2 \times (n+1) = 2n+2$ total conditions.
    
- **Resulting Polynomial:** To satisfy $2n+2$ conditions, we need a polynomial with $2n+2$ coefficients, which is a polynomial of degree (at most) $2n+1$.
    

---

### The Construction: Building $H(x)$

Just like Lagrange, we'll build $H(x)$ as a weighted sum. But this time, we have weights for both $f(x_i)$ and $f'(x_i)$:

$$H(x) = \sum_{i=0}^{n} \left[ \alpha_i(x) f(x_i) + \beta_i(x) f'(x_i) \right]$$

Our job is to find the _basis polynomials_ $\alpha_i(x)$ and $\beta_i(x)$.

To make this work, we need to enforce our $2n+2$ conditions. This leads to 4 requirements for our basis polynomials at any node $x_j$:

1. **$H(x_j) = f(x_j)$:**
    
    - We need the $f(x_j)$ term to be 1: $\alpha_j(x_j) = 1$.
        
    - All other $f(x_i)$ terms must be 0: $\alpha_i(x_j) = 0$ (for $i \neq j$).
        
    - All $f'(x_i)$ terms must be 0: $\beta_i(x_j) = 0$ (for all $i$).
        
2. **$H'(x_j) = f'(x_j)$:**
    
    - We need the $f'(x_j)$ term to be 1: $\beta'_j(x_j) = 1$.
        
    - All other $f'(x_i)$ terms must be 0: $\beta'_i(x_j) = 0$ (for $i \neq j$).
        
    - All $f(x_i)$ terms must be 0: $\alpha'_i(x_j) = 0$ (for all $i$).
        

---

### The "Aha!" Moment: Using $L_i(x)^2$

Your notes show the key insight. We need to find $\alpha_i(x)$ and $\beta_i(x)$ that satisfy these conditions. Let's look at the Lagrange polynomial $L_i(x)$.

- We know $L_i(x_j) = 0$ for $i \neq j$.
    
- If we use $(L_i(x))^2$, it's _still_ zero at $x_j$ (for $i \neq j$).
    
- Critically, the _derivative_ of $(L_i(x))^2$ is $2L_i(x)L'_i(x)$. At $x_j$ (for $i \neq j$), this derivative is $2L_i(x_j)L'_i(x_j) = 2 \cdot 0 \cdot L'_i(x_j) = 0$.
    

This $(L_i(x))^2$ term almost gives us what we need! It satisfies most of the "zero" conditions. We just need to multiply it by a simple linear factor $(ax+b)$ to fix the remaining conditions at $x = x_i$.

---

### Deriving the Basis Polynomials (as in your notes)

Your notes perfectly follow this logic to find the 4 unknown coefficients ($a_i, b_i, c_i, d_i$) for each $\alpha_i$ and $\beta_i$.

#### 1. Finding $\alpha_i(x) = (a_ix + b_i)(L_i(x))^2$

- **Condition:** $\alpha_i(x_i) = 1$
    
    - $(a_ix_i + b_i)(L_i(x_i))^2 = 1$
        
    - Since $L_i(x_i)=1$, this gives: $a_ix_i + b_i = 1$ (Your equation $\textcircled{1}$)
        
- **Condition:** $\alpha'_i(x_i) = 0$
    
    - First, get the derivative $\alpha'_i(x) = a_i(L_i(x))^2 + (a_ix + b_i)(2L_i(x)L'_i(x))$
        
    - Plug in $x_i$: $\alpha'_i(x_i) = a_i(L_i(x_i))^2 + (a_ix_i + b_i)(2L_i(x_i)L'_i(x_i))$
        
    - Sub in $L_i(x_i)=1$ and $a_ix_i+b_i=1$: $a_i(1)^2 + (1)(2 \cdot 1 \cdot L'_i(x_i)) = 0$
        
    - This simplifies to $a_i + 2L'_i(x_i) = 0$, which gives:
        
        - **$a_i = -2L'_i(x_i)$** (Your purple box)
            
- **Substitute $a_i$ back into $\textcircled{1}$:**
    
    - $(-2L'_i(x_i))x_i + b_i = 1$
        
    - **$b_i = 1 + 2x_iL'_i(x_i)$** (Your other purple box)
        

#### 2. Finding $\beta_i(x) = (c_ix + d_i)(L_i(x))^2$

Your notes set this up but don't complete it. Let's finish the derivation:

- **Condition:** $\beta_i(x_i) = 0$
    
    - $(c_ix_i + d_i)(L_i(x_i))^2 = 0$
        
    - Since $L_i(x_i)=1$, this gives: $c_ix_i + d_i = 0$
        
- **Condition:** $\beta'_i(x_i) = 1$
    
    - First, get the derivative $\beta'_i(x) = c_i(L_i(x))^2 + (c_ix + d_i)(2L_i(x)L'_i(x))$
        
    - Plug in $x_i$: $\beta'_i(x_i) = c_i(L_i(x_i))^2 + (c_ix_i + d_i)(2L_i(x_i)L'_i(x_i))$
        
    - Sub in $L_i(x_i)=1$ and $c_ix_i+d_i=0$: $c_i(1)^2 + (0)(2 \cdot 1 \cdot L'_i(x_i)) = 1$
        
    - This simplifies to: **$c_i = 1$**
        
- **Substitute $c_i$ back:**
    
    - $(1)x_i + d_i = 0$
        
    - **$d_i = -x_i$**
        

By finding these coefficients, you have successfully derived the Hermite basis polynomials.

Would you like to see how these coefficients $a_i, b_i$ and $c_i, d_i$ are typically simplified into their final, standard forms?
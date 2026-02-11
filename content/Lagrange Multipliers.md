---
publish: 1
entity_extraction_done: true
tags:
  - topic/math
---

## Lagrange Multipliers

*Kısıtlı optimizasyon yöntemi*

![[Lagrange Multipliers-20240528151750445.webp|413]]

Let the blue line represent the function f with the constraint x² + y² = 1. See the yellow lines that barely kiss the blue lines? Those are going to be where the maximum and minimum values of the function occurs. 

Check this out: Those curves that barely touch our function, their gradient at that spot is going to be the scalar multiple of the gradient of our curve in that spot. This is how Lagrange Multipliers works.

$$\nabla f = \lambda \nabla g$$

Bkz: [[Matematik]] • [[Categories/Vector Calculus/gradient|gradient]]
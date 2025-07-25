---
publish: 1
---

[[convolution sum]]


Okay, let's take a look at "Lecture 4 - LTI Systems" to give you a heads-up on the main topics covered.

Based on the document, this lecture focuses heavily on **Linear Time-Invariant (LTI) Systems** and a fundamental concept called **Convolution**. Here are the key ideas you'll encounter:

1. **Importance of LTI Systems:** These systems have both linearity (superposition holds) and time-invariance (system behavior doesn't change over time).

2. **Impulse Response is Key:** ==A central idea is that any LTI system can be completely characterized by its response to a single, simple signal:== the **unit impulse** ($\delta[n]$ in discrete-time, $\delta(t)$ in continuous-time). This response is called the **impulse response**, usually denoted by $h[n]$ or $h(t)$.

3. **Representing Signals with Impulses:** The lecture will show how arbitrary signals can be broken down and represented as a sum (in discrete-time) or integral (in continuous-time) of scaled and shifted unit impulses (the **sifting property**).

4. **Convolution Sum (Discrete-Time):** 
   By representing inputs as sums of impulses and using LTI properties, you can find the output $y[n]$ for *any* input $x[n]$ given the impulse response $h[n]$. This is the **convolution sum**:

   $$
   y[n] = \sum_{k=-\infty}^{\infty} x[k] \, h[n - k]
   $$

   often written as $y[n] = x[n] * h[n]$.

5. **Convolution Integral (Continuous-Time):**
   Similarly, for continuous-time LTI systems, the output is given by the **convolution integral**:

   $$
   y(t) = \int_{-\infty}^{\infty} x(\tau)\, h(t - \tau)\, d\tau
   $$

   often written as $y(t) = x(t) * h(t)$.

Essentially, this lecture introduces convolution as the fundamental operation describing how an LTI system transforms an input signal into an output signal, based on the system's impulse response.

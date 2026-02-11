---
publish: 1
entity_extraction_done: true
---


In AC circuit analysis, we use complex numbers (and complex exponentials) as a convenient way to represent sinusoidal voltages and currents. This makes the math easier because we can handle amplitude and phase information together.
When we use a complex exponential like `Vke^(jωt)` to represent a voltage, the real part of this expression, `Re{Vke^(jωt)}`, gives us the actual, physically measurable voltage waveform.

`x(t) = A₁e^(j(ω₁t + φ₁)) + A₂e^(j(ω₂t + φ₂)) + ... + Aₙe^(j(ωₙt + φₙ))`
- `A₁, A₂, ..., Aₙ` represent the amplitudes of each component.
- `ω₁, ω₂, ..., ωₙ` represent the angular frequencies of each component (ω = 2πf, where f is the frequency in Hz).
- `φ₁, φ₂, ..., φₙ` represent the phase shifts of each component.
- `j` is the imaginary unit (√-1).

- Notice it is j(wt + φ) and not jwt + φ.

Bkz: [[Matematik]] • [[Fizik]] • [[Engineering]]
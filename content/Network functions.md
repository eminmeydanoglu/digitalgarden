---
publish: 1
tags:
  - topic/circuits
  - topic/engineering
entity_extraction_done: true
---

 
In any linear, time-invariant (LTI) circuit, once you drive it with a sinusoid at angular frequency ω, **all** voltages and currents in the network will also be sinusoids at that same ω, but with different amplitudes and phase‐shifts. By representing them as complex **phasors** you can form **network functions**—ratios of an output phasor to an input phasor—which depend **only** on the circuit’s topology and component values, not on how large your input is.

Suppose you pick one “input” quantity (either a voltage or a current) and one “output” quantity. The four possibilities are:

1. Voltage‐to‐voltage transfer

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><msub><mi>H</mi><mi>V</mi></msub><mo stretchy="false">(</mo><mi>j</mi><mi>ω</mi><mo stretchy="false">)</mo><mtext>  </mtext><mo>=</mo><mtext>  </mtext><mfrac><mrow><msub><mi>V</mi><mrow><mi mathvariant="normal">o</mi><mi mathvariant="normal">u</mi><mi mathvariant="normal">t</mi></mrow></msub><mo stretchy="false">(</mo><mi>j</mi><mi>ω</mi><mo stretchy="false">)</mo></mrow><mrow><msub><mi>V</mi><mrow><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow></msub><mo stretchy="false">(</mo><mi>j</mi><mi>ω</mi><mo stretchy="false">)</mo></mrow></mfrac></mrow><annotation encoding="application/x-tex">  H_V(jω)\;=\;\frac{V_{\rm out}(jω)}{V_{\rm in}(jω)}</annotation></semantics></math>

tells you the gain (magnitude change) and phase shift that the circuit applies to an input voltage.

2. **Voltage‐to‐current transfer** (also called a **transfer admittance**)
	<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><msub><mi>Y</mi><mi>t</mi></msub><mo stretchy="false">(</mo><mi>j</mi><mi>ω</mi><mo stretchy="false">)</mo><mtext>  </mtext><mo>=</mo><mtext>  </mtext><mfrac><mrow><msub><mi>I</mi><mrow><mi mathvariant="normal">o</mi><mi mathvariant="normal">u</mi><mi mathvariant="normal">t</mi></mrow></msub><mo stretchy="false">(</mo><mi>j</mi><mi>ω</mi><mo stretchy="false">)</mo></mrow><mrow><msub><mi>V</mi><mrow><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow></msub><mo stretchy="false">(</mo><mi>j</mi><mi>ω</mi><mo stretchy="false">)</mo></mrow></mfrac></mrow><annotation encoding="application/x-tex">  Y_{t}(jω)\;=\;\frac{I_{\rm out}(jω)}{V_{\rm in}(jω)}</annotation></semantics></math>
3. Current‐to‐current transfer
	<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><msub><mi>H</mi><mi>I</mi></msub><mo stretchy="false">(</mo><mi>j</mi><mi>ω</mi><mo stretchy="false">)</mo><mtext>  </mtext><mo>=</mo><mtext>  </mtext><mfrac><mrow><msub><mi>I</mi><mrow><mi mathvariant="normal">o</mi><mi mathvariant="normal">u</mi><mi mathvariant="normal">t</mi></mrow></msub><mo stretchy="false">(</mo><mi>j</mi><mi>ω</mi><mo stretchy="false">)</mo></mrow><mrow><msub><mi>I</mi><mrow><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow></msub><mo stretchy="false">(</mo><mi>j</mi><mi>ω</mi><mo stretchy="false">)</mo></mrow></mfrac></mrow><annotation encoding="application/x-tex">  H_I(jω)\;=\;\frac{I_{\rm out}(jω)}{I_{\rm in}(jω)}</annotation></semantics></math>
4. **Current‐to‐voltage transfer** (also called a **transfer impedance**)
	<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><msub><mi>Z</mi><mi>t</mi></msub><mo stretchy="false">(</mo><mi>j</mi><mi>ω</mi><mo stretchy="false">)</mo><mtext>  </mtext><mo>=</mo><mtext>  </mtext><mfrac><mrow><msub><mi>V</mi><mrow><mi mathvariant="normal">o</mi><mi mathvariant="normal">u</mi><mi mathvariant="normal">t</mi></mrow></msub><mo stretchy="false">(</mo><mi>j</mi><mi>ω</mi><mo stretchy="false">)</mo></mrow><mrow><msub><mi>I</mi><mrow><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow></msub><mo stretchy="false">(</mo><mi>j</mi><mi>ω</mi><mo stretchy="false">)</mo></mrow></mfrac></mrow><annotation encoding="application/x-tex">  Z_{t}(jω)\;=\;\frac{V_{\rm out}(jω)}{I_{\rm in}(jω)}</annotation></semantics></math>
	
Bkz: [[Engineering]] • [[Matematik]] • [[Fizik]]
	
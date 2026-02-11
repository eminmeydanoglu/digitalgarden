---
publish: 1
tags:
  - topic/math
---

If your response consists of mathematical signs and notations, I'd like you to give me your response in two versions:

**1. Normal Output:**  
Use standard Markdown formatting. Include things like headings (`##`), bold, italics, and math with LaTeX syntax using `$...$` (inline) and `$$...$$` (block).

**2. Obsidian-Compatible Code Block:**  
Immediately after the normal version, repeat the exact same content, but wrap it in a Markdown code block using triple backticks (```markdown at the top and ``` at the bottom). This ensures that when I paste it into Obsidian, all formatting is preserved. Don't escape characters. Just preserve the original formatting within the code block.

This is important for preserving math rendering like:
- `$y[n] = x[n] * h[n]$` (inline)
- `$$ y(t) = \int_{-\infty}^{\infty} x(\tau)h(t - \tau)\, d\tau $$` (block)

Make sure both versions appear one after another in your response.


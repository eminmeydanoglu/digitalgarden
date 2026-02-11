---
publish: 1
tags:
  - topic/math
entity_extraction_done: true
---

See also: [[Linear Algebra]], [[AUV]], [[column space, null space, solution space]]

"For $\mathbb{R}^n$, $S=\{\vec{e}_1, \vec{e}_2, \dots, \vec{e}_n\}$ form a basis. Where $\vec{e}_i = [0, \dots, 1, \dots, 0]^T$ ($i$-th element is 1)."
### **$\mathbb{R}^3$ Örneği ve İspat**
 $\mathbb{R}^3$'teki standart bazın gerçekten bir baz olduğunu ispatlıyor.

**1. Lineer Bağımsızlık Testi (Determinant Yöntemi):**

> **Tahtadan Alıntı:** _"Linear independence: $|A| = \det(I) = 1 \neq 0, \implies \vec{i}, \vec{j}, \vec{k}$ are linearly independent."_

Analiz:

Vektörleri sütun olarak yan yana dizdiğinde bir Birim Matris (Identity Matrix) oluşur. Birim matrisin determinantı 1'dir. Determinant 0 olmadığı için bu vektörler kesinlikle bağımsızdır. Yani hiçbiri diğerinin alternatifi değildir.
**2. Germe (Span) Testi:**

> **Tahtadan Alıntı:** _"Let $\vec{v} = [x, y, z]^T \in \mathbb{R}^3$. If $\vec{v}$ can be written as a linear combination of $\vec{v}_1, \vec{v}_2, \vec{v}_3$..."_

Analiz:

Herhangi bir $[x, y, z]$ vektörünü şu şekilde yazabilirsin:

$$\begin{bmatrix} x \\ y \\ z \end{bmatrix} = x \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} + y \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} + z \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$$

Bu, uzaydaki her noktanın bu üç vektörle tanımlanabileceğini kanıtlar.

Mühendislik Bağlantısı (Robotik Frame):

AUV'nin üzerindeki sensörler (IMU, DVL) kendi yerel eksenlerine (Body Frame) göre veri basar. Bu yerel eksen aslında bir "Standart Baz"dır ($\vec{i}, \vec{j}, \vec{k}$). Robotun "ileri" gitmesi, $\vec{i}$ yönünde katsayıyı artırmak demektir.


---
> _"If we choose $S = \{t^2, t, 1\}$ ... $S$ is known as the NATURAL (or STANDARD) basis for $P_2$."_

Analiz:

$P_2$ uzayı, derecesi en fazla 2 olan polinomların (parabollerin) dünyasıdır ($at^2 + bt + c$).

Burada "vektörlerimiz" şunlardır:

- $\vec{v}_1 = t^2$
    
- $\vec{v}_2 = t$
    
- $\vec{v}_3 = 1$
    

Bunlar lineer bağımsızdır çünkü $t^2$'yi, $t$ ve $1$ kullanarak elde edemezsin (biri eğri, biri doğru, biri sabit).

Genelleme: $P_n$ uzayının boyutu $n+1$'dir.
Boyut, bir sistemi tarif etmek için gereken **minimum bağımsız parametre sayısıdır**. Eğer AUV su altında serbestçe yüzüyorsa (x, y, z, roll, pitch, yaw), onun durum uzayı (state space) 6 boyutludur. Bu uzayı tanımlamak için 6 tane bağımsız baz vektörüne ihtiyacın vardır. Eğer sensörlerinden biri bozulursa ve diğer sensörlerin kombinasyonuyla o veriyi üretemiyorsan, "Boyut Kaybı" yaşarsın ve robotun o eksende kör olur.
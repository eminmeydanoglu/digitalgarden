---
publish: 1
---

Bayes kuralı, olasılık teorisinde, bir hipotezin verilere dayalı olarak güncellenmesine olanak tanır. Başlangıçtaki inançlarımızı, yeni bilgilerle nasıl değiştireceğimizi gösterir. Matematiksel ifadesi aşağıdaki gibidir:


$$ 
P(H | E) = \frac{P(E | H) \cdot P(H)}{P(E)}
$$

Burada:

- \( P(H | E) \) = Hipotez \( H \)'nin, kanıt \( E \) verildiğinde olasılığı (posterior olasılık).
- \( P(E | H) \) = Kanıt \( E \)'nin, hipotez \( H \) doğru olduğunda gözlenme olasılığı (likelihood).
- \( P(H) \) = Hipotez \( H \)'nin, kanıt olmadan önceki olasılığı (prior olasılık).
- \( P(E) \) = Kanıt \( E \)'nin gözlenme olasılığı (marginal likelihood).

### Örnek

Diyelim ki bir tıbbi test, bir hastalığı %99 doğrulukla tespit ediyor. Hastalığın popülasyonda %1 oranında yaygın olduğunu biliyoruz. Bir kişinin testi pozitif çıkarsa, bu kişinin gerçekten hasta olma olasılığı nedir?

- \( P(H) = 0.01 \): Kişinin hasta olma olasılığı.
- \( P(E | H) = 0.99 \): Testin hasta bir kişide pozitif çıkma olasılığı.
- \( P(E | \neg H) = 0.01 \): Testin sağlıklı bir kişide yanlış pozitif çıkma olasılığı.
- \( P(\neg H) = 0.99 \): Kişinin sağlıklı olma olasılığı.

Öncelikle, \( P(E) \)'yi hesaplamamız gerekiyor:

$$
P(E) = P(E | H) \cdot P(H) + P(E | \neg H) \cdot P(\neg H)
$$
$$
P(E) = 0.99 \cdot 0.01 + 0.01 \cdot 0.99 = 0.0198
$$

Sonra, Bayes kuralını kullanarak \( P(H | E) \)'yi bulalım:

$$
P(H | E) = \frac{P(E | H) \cdot P(H)}{P(E)}
$$
$$
P(H | E) = \frac{0.99 \cdot 0.01}{0.0198} \approx 0.5
$$

Bu durumda, testin pozitif çıkması durumunda kişinin gerçekten hasta olma olasılığı %50'dir. Bu örnek, bir testin doğruluğu ve hastalığın popülasyondaki yaygınlığı arasındaki ilişkinin nasıl değerlendirileceğini gösterir.
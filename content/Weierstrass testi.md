---
etiketler:
publish: 1
entity_extraction_done: true
---

# Weierstrass M-Testi

Weierstrass M-Testi, bir **fonksiyon serisinin** $\sum f_n(x)$ **düzgün yakınsaklığını** kanıtlamak için kullanılan en yaygın ve en güçlü araçlardan biridir.

Temel fikri şudur: Eğer fonksiyon serisinin her bir terimini $x$'ten bağımsız (sabit) ve **yakınsak bir sayı serisinin** terimleriyle "üstten bastırabilirsek" (dominate edebilirsek), o zaman fonksiyon serimiz **düzgün yakınsar**.

Bu test, karmaşık bir fonksiyon serisinin düzgün yakınsaklık problemini, daha basit bir *sayı serisinin* yakınsaklık problemine indirger.

> [!info] Teoremin İfadesi
> $I$ bir aralık olmak üzere, $\sum_{n=1}^{\infty} f_n(x)$ bir fonksiyon serisi olsun.
>
> Eğer $\forall n \ge 1$ ve $\forall x \in I$ için,
> $$ |f_n(x)| \le M_n $$
> şartını sağlayan ( $x$'ten bağımsız) pozitif terimli bir $\{M_n\}$ **sayı dizisi** varsa
>
> **VE**
>
> $\sum_{n=1}^{\infty} M_n$ sayı serisi **YAKINSAK** ise,
>
> O zaman $\sum_{n=1}^{\infty} f_n(x)$ fonksiyon serisi $I$ aralığı üzerinde **HEM DÜZGÜN YAKINSAKTIR HEM DE MUTLAK YAKINSAKTIR**.

---

## 🎯 Testin Uygulama Adımları

1.  **Aday $M_n$ Bulma:**
    $f_n(x)$ fonksiyonunun $I$ aralığı üzerindeki maksimum (supremum) değerini bulmaya çalışırız. Genellikle $M_n$ şöyle seçilir:
    $$ M_n = \sup_{x \in I} |f_n(x)| $$
    Bu, $M_n$'nin $x$'e bağlı olmamasını garantiler. $f_n(x)$'in $x$'e göre türevini alıp 0'a eşitleyerek bu maksimum değeri bulabiliriz.

2.  **Sayı Serisini Test Etme:**
    $\sum M_n$ sayı serisini oluştururuz. Bu serinin yakınsak olup olmadığını [[Seri Testleri]] (örneğin Oran Testi, Kök Testi, p-Serisi Testi, LKT) kullanarak kontrol ederiz.

3.  **Sonuç:**
    * Eğer $\sum M_n$ **yakınsak** ise $\implies$ Weierstrass M-Testi'ne göre $\sum f_n(x)$ serisi $I$ üzerinde **düzgün yakınsaktır**.
    * Eğer $\sum M_n$ **ıraksak** ise $\implies$ **Test sonuç vermez (Inconclusive)**. Düzgün yakınsak *olabilir* de, *olmayabilir* de. Başka bir yöntem denemek gerekir. (Testin başarısız olması, serinin düzgün yakınsak olmadığını *kanıtlamaz*.)

---

## 💡 Örnekler

### Örnek 1: $\sum_{n=1}^{\infty} \frac{\sin(nx)}{n^2}$ serisi $\mathbb{R}$ üzerinde

1.  **$M_n$ Bulma:**
    $I = \mathbb{R}$ (tüm reel sayılar).
    $$ |f_n(x)| = \left| \frac{\sin(nx)}{n^2} \right| = \frac{|\sin(nx)|}{n^2} $$
    $x$ ne olursa olsun, $|\sin(nx)| \le 1$ olduğunu biliyoruz.
    $$ |f_n(x)| \le \frac{1}{n^2} $$
    O halde, $x$'ten bağımsız $M_n = \frac{1}{n^2}$ olarak seçebiliriz.

2.  **$\sum M_n$ Testi:**
    Sayı serisi $\sum_{n=1}^{\infty} M_n = \sum_{n=1}^{\infty} \frac{1}{n^2}$'dir.
    Bu, bir **p-serisidir** ve $p=2 > 1$ olduğu için **YAKINSAKTIR**.

3.  **Sonuç:**
    $\sum M_n$ yakınsak olduğundan, Weierstrass M-Testi'ne göre $\sum \frac{\sin(nx)}{n^2}$ serisi $\mathbb{R}$ üzerinde **düzgün yakınsaktır**.

### Örnek 2: $\sum_{n=1}^{\infty} e^{nx}$ serisi $[-2, -1]$ aralığında

(Bir önceki sorudaki durumun kısıtlanmış hali)

1.  **$M_n$ Bulma:**
    $I = [-2, -1]$.
    $f_n(x) = e^{nx}$ fonksiyonu $x$'e göre artan bir fonksiyondur (çünkü $n > 0$). Bu nedenle, kapalı aralıktaki maksimum değerini sağ uç noktada ($x = -1$) alır.
    $$ |f_n(x)| = e^{nx} \le e^{n(-1)} = e^{-n} = \left(\frac{1}{e}\right)^n $$
    O halde, $M_n = (1/e)^n$ seçebiliriz.

2.  **$\sum M_n$ Testi:**
    Sayı serisi $\sum_{n=1}^{\infty} M_n = \sum_{n=1}^{\infty} \left(\frac{1}{e}\right)^n$'dir.
    Bu, ortak oranı $r = 1/e \approx 1/2.718 < 1$ olan bir **geometrik seridir**. Bu nedenle **YAKINSAKTIR**.

3.  **Sonuç:**
    $\sum M_n$ yakınsak olduğundan, Weierstrass M-Testi'ne göre $\sum e^{nx}$ serisi $[-2, -1]$ aralığında **düzgün yakınsaktır**.

> [!warning] Örnek 2'nin Tuzağı
> Eğer aralığı $I = [-2, 0)$ olarak alsaydık:
> $M_n = \sup_{x \in [-2, 0)} |e^{nx}| = \sup_{x \in [-2, 0)} e^{nx} = e^{n \cdot 0} = 1$
> $\sum M_n = \sum 1$ serisi **ıraksaktır**.
> Bu durumda Weierstrass M-Testi **sonuç vermezdi**. (Bu, serinin düzgün yakınsak olmadığını kanıtlamaz, sadece testin çalışmadığını gösterir. $x=0$ civarındaki davranış için $n$. terim testine bakmamız gerekir.)

## İlgili Konular
- [[Düzgün Yakınsaklık]]
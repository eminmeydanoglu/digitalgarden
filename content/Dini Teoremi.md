---
publish: 1
tags:
  - type/index
entity_extraction_done: true
---
---
etiketler:   #düzgün-yakınsaklık
kaynak: "Louis Brand, Sayfa 404"
---

# Dini Teoremi

Dini Teoremi, **noktasal yakınsaklığın** hangi özel koşullar altında **düzgün yakınsaklığa** dönüştüğünü belirten güçlü bir araçtır. Özellikle $[a, b]$ gibi kapalı ve sınırlı (kompakt) kümeler üzerinde çalışırken çok kullanışlıdır.

> [!info] Teoremin İfadesi
> $\{f_n(x)\}$ fonksiyon dizisinin terimleri ve bu dizinin limit fonksiyonu $f(x)$, $[a, b]$ kapalı aralığında **sürekli** olsun.
>
> Eğer $\{f_n(x)\}$ dizisi $[a, b]$'de **monoton** (azalan veya artan) ise, $\{f_n(x)\}$ dizisi $[a, b]$'de $f(x)$'e **düzgün olarak** yakınsar.

**Teoremin Koşulları (Özet):**
1.  **Kompakt Küme:** Aralık $[a, b]$ gibi kapalı ve sınırlı olmalıdır.
2.  **$f_n$ Sürekliliği:** Dizideki her $f_n(x)$ fonksiyonu $[a, b]$ üzerinde sürekli olmalıdır.
3.  **$f$ Sürekliliği:** Dizinin noktasal limiti olan $f(x)$ fonksiyonu da $[a, b]$ üzerinde sürekli olmalıdır.
4.  **Monotonluk:** Her bir $x \in [a, b]$ için, $f_n(x)$ dizisi $n$'ye göre monoton olmalıdır (yani, $f_n(x) \le f_{n+1}(x)$ veya $f_n(x) \ge f_{n+1}(x)$ olmalıdır).

Eğer bu dört koşul sağlanırsa, sonuç **düzgün yakınsaklıktır**.

---

## Örnek: $f_n(x) = \frac{x}{1+nx^2}$

Görseldeki örneği inceleyelim. $f_n(x) = \frac{x}{1+nx^2}$ fonksiyon dizisinin $x \in [0, 1]$ aralığında düzgün yakınsaklığını Dini Teoremi ile araştıralım.

Dini Teoremi'nin koşullarını tek tek kontrol edelim:

### 1. Aralık (Kompakt Küme)
Çalıştığımız aralık $x \in [0, 1]$'dir. Bu aralık **kapalı ve sınırlıdır** (kompakt).
(✔️ Koşul 1 sağlandı.)

### 2. $f_n(x)$ Fonksiyonlarının Sürekliliği
$f_n(x) = \frac{x}{1+nx^2}$ rasyonel bir fonksiyondur. Paydası olan $1+nx^2$, $x \in [0, 1]$ ve $n \ge 1$ için daima $1+nx^2 \ge 1$'dir.
Payda hiçbir zaman sıfır olmaz. Bu nedenle, her bir $f_n(x)$ fonksiyonu $[0, 1]$ aralığında **süreklidir**.
(✔️ Koşul 2 sağlandı.)

### 3. Noktasal Limit $f(x)$ ve Sürekliliği
Dizinin noktasal limitini bulalım:
$f(x) = \lim_{n\to\infty} f_n(x) = \lim_{n\to\infty} \frac{x}{1+nx^2}$

* **Eğer $x = 0$ ise:** $f_n(0) = \frac{0}{1+0} = 0$. $\lim_{n\to\infty} 0 = 0$.
* **Eğer $x \in (0, 1]$ ise:** Pay sabit ($x$) iken, payda ($1+nx^2$) $n \to \infty$ iken sonsuza gider.
    $$ \lim_{n\to\infty} \frac{x}{1+nx^2} = 0 $$

Sonuç olarak, noktasal limit fonksiyonu $f(x) = 0$'dır.
$f(x) = 0$ (sabit fonksiyon), $[0, 1]$ aralığında **süreklidir**.
(✔️ Koşul 3 sağlandı.)

### 4. Monotonluk
Şimdi, dizinin $n$'ye göre monotonluğunu inceleyelim. $f_n(x)$ ve $f_{n+1}(x)$'i karşılaştıralım:
$$ f_n(x) = \frac{x}{1+nx^2} $$
$$ f_{n+1}(x) = \frac{x}{1+(n+1)x^2} = \frac{x}{1+nx^2+x^2} $$

$x \in [0, 1]$ aralığında $x^2 \ge 0$ olduğundan:
$$ 1+nx^2+x^2 \ge 1+nx^2 $$
Paydalar pozitif olduğundan ve $f_{n+1}$'in paydası daha büyük (veya $x=0$ ise eşit) olduğundan, kesrin değeri daha küçük olacaktır:
$$ f_{n+1}(x) \le f_n(x) \quad \forall x \in [0, 1] $$
Bu, dizinin **monoton azalan** olduğunu gösterir.
(✔️ Koşul 4 sağlandı.)

### Sonuç
Dini Teoremi'nin **tüm koşulları sağlandığı için**, $f_n(x) = \frac{x}{1+nx^2}$ dizisi, $f(x) = 0$ fonksiyonuna $[0, 1]$ aralığında **düzgün yakınsar (D.Y.)**.

## İlgili Konular
- [[Düzgün Yakınsaklık]]

Bkz: [[Matematik]]
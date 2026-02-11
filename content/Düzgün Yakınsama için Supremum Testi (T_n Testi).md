---
publish: 1
tags:
  - type/index
entity_extraction_done: true
---
ÇOK İYİ NOT 

**Etiketler:** #matematiksel-analiz   

## 1. Temel Fikir

Bir $f_n(x)$ fonksiyon dizisinin $f(x)$ fonksiyonuna **noktasal yakınsaması**, her bir $x$ noktasının *kendi hızında* $f(x)$'e yaklaşması demektir.

**Düzgün yakınsama** ise çok daha güçlü bir koşuldur: Tüm $x$ noktalarının "aynı anda", "kolektif" bir şekilde $f(x)$'e yaklaşmasını ister.

$T_n$ (veya $M_n$) testi, bu "kolektif" yakınsamanın en kötü durumunu ölçen bir araçtır.

## 2. T_n Testinin Tanımı

$f_n$ dizisi $D$ tanım kümesi üzerinde $f$ fonksiyonuna noktasal yakınsasın. $T_n$ (veya $M_n$) terimi şu şekilde tanımlanır:

$$T_n = \sup_{x \in D} |f_n(x) - f(x)|$$

**Bu ne demektir?**
$T_n$, $f_n(x)$ fonksiyonu ile limit fonksiyonu $f(x)$ arasındaki farkın (yani "hata") $D$ kümesi üzerindeki **en büyük** (supremum) değeridir. $T_n$'e o $n$. adımdaki "maksimum hata" olarak bakabiliriz.

## 3. Ana Teorem (Testin Kuralı)

$f_n$ dizisinin $f$'e **düzgün yakınsaması** için gerek ve yeter koşul:

> $$\lim_{n \to \infty} T_n = 0$$

Yani, "en kötü hata"nın ($T_n$) kendisi $n$ sonsuza giderken sıfıra yaklaşıyorsa, yakınsama **düzgündür**. Eğer sıfırdan farklı bir sabite yaklaşıyor veya 0'a gitmiyorsa, yakınsama **düzgün değildir**.

---

## 4. Testin Pratik Uygulaması

Bu teoremi iki temel senaryoda kullanırız:

### Senaryo A: Düzgün Yakınsaklığı ÇÜRÜTMEK (Hızlı Yol)

**Hedef:** $\lim_{n \to \infty} T_n \ne 0$ olduğunu göstermek.

Bunun için $T_n$'nin tam değerini (supremum) bulmak zorunda değiliz. $T_n$'nin tanımı gereği, *herhangi bir* $x$ için $T_n \ge |f_n(x) - f(x)|$ olduğunu biliyoruz.

**Strateji:**
1.  $n$'ye bağlı özel bir nokta ($x_n$) seçeriz. Bu $x_n$ noktası genellikle $f_n(x)$'in "tepe noktasını" veya "en çok saptığı" yeri temsil eder.
2.  $T_n \ge |f_n(x_n) - f(x_n)|$ eşitsizliğini kullanırız.
3.  $|f_n(x_n) - f(x_n)|$ değerinin $n \to \infty$ iken 0'dan farklı bir sabite (örneğin $1$, $1/2$, $1/e$) gittiğini gösteririz.
4.  **Sonuç:** Eğer $\lim |f_n(x_n) - f(x_n)| = C \ne 0$ ise, o zaman $\lim T_n \ge C$ olmalıdır. $\lim T_n \ne 0$ olduğu için yakınsama **DÜZGÜN DEĞİLDİR**.

**Örnekler:**
* $f_n(x) = \frac{2nx^2}{n^2x^4+1}$, $f(x)=0$.
    * $x_n = \frac{1}{\sqrt{n}}$ seç.
    * $|f_n(x_n) - 0| = \left| \frac{2n(1/n)}{n^2(1/n^2)+1} \right| = \frac{2}{1+1} = 1$.
    * $T_n \ge 1$ $\implies$ $\lim T_n \ge 1$ ($\ne 0$). Düzgün değil.
* $f_n(x) = \frac{x}{n} e^{-|x|/n}$, $f(x)=0$.
    * $x_n = n$ seç.
    * $|f_n(x_n) - 0| = \left| \frac{n}{n} e^{-|n|/n} \right| = e^{-1} = \frac{1}{e}$.
    * $T_n \ge \frac{1}{e}$ $\implies$ $\lim T_n \ge \frac{1}{e}$ ($\ne 0$). Düzgün değil.

---

### Senaryo B: Düzgün Yakınsaklığı KANITLAMAK (Zor Yol)

**Hedef:** $\lim_{n \to \infty} T_n = 0$ olduğunu göstermek.

1.  $g_n(x) = |f_n(x) - f(x)|$ fark fonksiyonunu tanımla.
2.  Bu $g_n(x)$ fonksiyonunun $x$'e göre türevini alıp sıfıra eşitleyerek maksimum değerini bul. Bu maksimum değer $T_n$'dir.
3.  Bulunan $T_n$ (ki $n$'ye bağlı bir ifade olmalı) ifadesinin $\lim_{n \to \infty} T_n = 0$ olduğunu göster.

**Örnek:**
* $f_n(x) = \frac{2x}{\pi} \arctan(nx)$, $f(x)=|x|$.
* $T_n = \sup_{x \in \mathbb{R}} \left| \frac{2x}{\pi} \arctan(nx) - |x| \right|$
* (Zorlu bir analizden sonra) $T_n = \frac{2}{n\pi}$ bulunur.
* $\lim_{n \to \infty} T_n = \lim_{n \to \infty} \frac{2}{n\pi} = 0$.
* **Sonuç:** Yakınsama **DÜZGÜNDÜR**.

---

## 5. Hızlı Alternatif: Süreklilik Testi

$T_n$ testine girmeden önce her zaman şu teoremi kontrol et:

> **Teorem:** Eğer dizideki her $f_n(x)$ fonksiyonu **sürekli** ise, ama noktasal limit fonksiyonu $f(x)$ **süreksiz** ise, yakınsama **DÜZGÜN OLAMAZ**.

Bu, $T_n$ hesabı yapmaktan çok daha hızlı bir çürütme yöntemidir.

**Örnek:**
* $f_n(x) = \frac{nx^2+1}{nx+1}$, $x \in [0,1]$.
* $f_n(x)$ fonksiyonları $[0,1]$ üzerinde süreklidir.
* Noktasal limit: $f(x) = \begin{cases} 1, & x=0 \\ x, & x \in (0, 1] \end{cases}$
* $f(x)$ fonksiyonu $x=0$ noktasında **süreksizdir**.
* **Sonuç:** $T_n$ hesabına gerek yok, yakınsama **DÜZGÜN DEĞİLDİR**.
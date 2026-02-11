---
publish: 1
tags:
  - type/index
entity_extraction_done: true
---

See also: [[Yakınsaklık Türleri ve Hiyerarşisi]], [[Düzgün yakınsamada sınırlılık]], [[Cauchy dizileri]]

### Teorem 1: Düzgün Yakınsaklık, Noktasal Yakınsaklıktan Güçlüdür

> **Alıntı (Teorem):** "Eğer $\{f_n\}$ fonksiyon dizisi $f$'e **düzgün** yakınsıyor ise, $\{f_n\}$ $f$'e **noktasal** olarak yakınsar." 1

Açıklaması (Sezgisel Anlamı):

Bu teorem, iki yakınsaklık türü arasındaki hiyerarşiyi belirler.

- **Düzgün Yakınsaklık (DY):** "Güçlü" koşuldur. Bütün $x$ noktalarının limite "aynı hızda" ve "birlikte" yaklaşmasını ister. $N$ eşiği _tüm $x$'ler için ortaktır_ ($N(\epsilon)$).
    
- **Noktasal Yakınsaklık (NY):** "Zayıf" koşuldur. Her $x$ noktasının limite "kendi hızında" yaklaşmasına izin verir. $N$ eşiği _her $x$ için farklı olabilir_ ($N(\epsilon, x)$).


Anahtar: HIZ. 

Teorem diyor ki: Eğer "güçlü" olan DY koşulu sağlanıyorsa, "zayıf" olan NY koşulu _otomatik olarak_ sağlanmış olur.

### İspatın Adımları (Neden DY $\implies$ NY?)

İspat, DY'nin tanımının NY'nin tanımını zaten içerdiğini gösterir.

Adım 1: DY'nin Tanımı (Elimizde Ne Var?)

Düzgün yakınsaklığın tanımı şudur22:

"Siz bana bir $\epsilon$ hata payı verdiğinizde, ben size tüm $x$'ler için ortak olan bir $N(\epsilon)$ eşiği bulabilirim. Bu $N$'den sonraki her $n$ için, $|f_n(x) - f(x)|$ hatası bütün $x$'ler için aynı anda $\epsilon$'dan küçük kalır." 3

Adım 2: NY'nin Tanımı (Neyi Kanıtlamak İstiyoruz?)

Noktasal yakınsaklık ise şunu ister4:

"Siz bana bir $\epsilon$ ve belirli bir $x_0$ noktası verdiğinizde, ben size o $x_0$'a özel bir $N$ eşiği bulabilirim. O $N$'den sonraki her $n$ için $|f_n(x_0) - f(x_0)|$ hatası $\epsilon$'dan küçük kalır." 5

Adım 3: İkisini Birleştirmek (Mantık)

İspat şöyle ilerler:

1. NY'yi kanıtlamak için, aralıktan rastgele _tek bir_ $x_0$ noktası seçelim6.
    
2. Bizim elimizde DY'nin garantisi var: _tüm $x$'ler için ortak çalışan_ bir $N(\epsilon)$ eşiğimiz zaten mevcut7777.
    
3. Eğer bu $N(\epsilon)$ eşiği _tüm $x$'ler_ için çalışıyorsa, o zaman bizim seçtiğimiz _o tek $x_0$ noktası için de_ çalışmak zorundadır8.
    
4. Bu durumda, $x_0$ noktamız için bir $N$ eşiği bulmuş olduk (o ortak $N$'yi kullandık).
    
5. Bu, tam olarak $x_0$ noktasında noktasal yakınsaklığın tanımıdır9.
    
6. $x_0$'ı rastgele seçtiğimiz için, bu mantık aralıktaki _tüm_ $x$ noktaları için geçerlidir. Dolayısıyla dizi noktasal yakınsaktır10.
    

> **Alıntı (İspatın Özeti):** "Bu kadar — yani düzgün yakınsama tanımındaki '$\exists N$ tüm $x$ için ortak' ifadesi, noktasal yakınsamanın gerektirdiği 'her $x$ için bir $N$ bulunur' şartı sağlanmış oldu." 11

### "Dikkat!" Kısmı (Tersi Doğru Değil)

> **Alıntı (Slayt):** "NY $\implies$ DY" (üzeri çizili) 12

Açıklaması:

Teoremin tersi doğru değildir.

Sadece "noktasal yakınsak" (NY) olması, "düzgün yakınsak" (DY) olduğu anlamına gelmez13.

Neden?

Noktasal yakınsaklıkta, her $x$ noktasının limite "kendi hızıyla" yakınsamasına izin verilir.

- $x=0.1$ için $N=10$ gerekebilir.
    
- $x=0.5$ için $N=100$ gerekebilir.
    
- $x=0.9$ için $N=1,000,000$ gerekebilir.
    

Eğer yakınsama hızı $x$'e bağlı olarak sürekli yavaşlıyorsa (gittikçe daha büyük $N$'ler gerekiyorsa), o zaman _tüm $x$'ler için ortak çalışan tek bir $N$ eşiği_ bulamayız. Bu durumda dizi NY olur, ama DY olmaz. (Örnek 2'deki $f_n(x)=x^n$ gibi).
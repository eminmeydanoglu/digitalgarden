---
publish: 1
tags:
  - type/index
entity_extraction_done: true
---


![[Pasted image 20251016172234.png]]
![[Pasted image 20251016172239.png]]
Bu teorem, "limit" ve "sürekli fonksiyon" (continuous function) kavramlarını birbirine bağlayan çok güçlü bir araçtır.

#### Teoremin Anlamı Nedir?

Teorem diyor ki: Elimizde bir $L$ sayısına yakınsayan (converging) bir $\{a_n\}$ dizisi varsa ve bu $L$ noktasında sürekli olan bir $f$ fonksiyonumuz varsa, o zaman $f(a_n)$ dizisi de $f(L)$ değerine yakınsar.

Basitçe söylemek gerekirse, **eğer bir fonksiyon sürekliyse, limiti fonksiyonun içine "atabilirsiniz"**.

Matematiksel olarak:

$$\lim_{n \to \infty} f(a_n) = f\left(\lim_{n \to \infty} a_n\right)$$

Bu eşitliğin geçerli olabilmesi için iki kritik şart vardır:

1. İçerideki $\{a_n\}$ dizisinin bir limiti ($L$) olmalı.
    
2. Dışarıdaki $f$ fonksiyonu bu $L$ limit noktasında sürekli olmalı.
    

#### Örnek Analizi

Görseldeki örneği inceleyelim:

$$\lim_{n \to \infty} \sqrt{\frac{n}{2n+1}}$$

Bu problemi teorem 3'ü kullanarak nasıl çözebiliriz?

1. **İç Dizi ve Dış Fonksiyonu Belirleyelim:**
    
    - İçerideki dizi: $a_n = \frac{n}{2n+1}$
        
    - Bu diziyi "içine alan" dış fonksiyon: $f(x) = \sqrt{x}$
        
2. İç Dizinin Limitini Bulalım:
    
    an​'in limitini hesaplayalım. Payı ve paydayı en yüksek dereceli terim olan n'e bölebiliriz:
    
    $$L = \lim_{n \to \infty} a_n = \lim_{n \to \infty} \frac{n}{2n+1} = \lim_{n \to \infty} \frac{\frac{n}{n}}{\frac{2n}{n} + \frac{1}{n}} = \lim_{n \to \infty} \frac{1}{2 + \frac{1}{n}}$$
    
    n→∞ iken n1​→0 olacağından, limit:
    
    $$L = \frac{1}{2+0} = \frac{1}{2}$$
    
    Dizimiz 21​'ye yakınsıyor.
    
3. Dış Fonksiyonun Sürekliliğini Kontrol Edelim:
    
    Dış fonksiyonumuz f(x)=x​. Bu fonksiyon, dizinin limiti olan L=21​ noktasında sürekli midir? Evet, köklü fonksiyonlar tanımlı oldukları pozitif sayılarda süreklidir.
    
4. Teoremi Uygulayalım:
    
    Tüm şartlar sağlandığı için limiti fonksiyonun içine alabiliriz:
    
    $$\lim_{n \to \infty} \sqrt{\frac{n}{2n+1}} = \sqrt{\lim_{n \to \infty} \frac{n}{2n+1}} = \sqrt{\frac{1}{2}} = \frac{1}{\sqrt{2}}$$
    
    Görseldeki çözüm de tam olarak bunu yapıyor.
    

---

### Teorem 4: Fonksiyon Limitinden Dizi Limitine Geçiş

Bu teorem, fonksiyonların limitleri (calculus'ta $x \to \infty$ durumu) ile dizilerin limitleri ($n \to \infty$ durumu) arasında bir köprü kurar.

#### Teoremin Anlamı Nedir?

Teorem şunu söyler: Eğer bir $f(x)$ fonksiyonunun $x \to \infty$ iken limiti $L$ ise ve biz bu fonksiyondaki $x$ yerine tamsayılar ($n$) koyarak bir $a_n=f(n)$ dizisi oluşturursak, bu dizinin limiti de $L$ olur.

**Sezgisel olarak:** Eğer bir fonksiyonun grafiği $x$ sonsuza giderken $y=L$ yatay çizgisine (horizontal asymptote) yaklaşıyorsa, bu grafiğin üzerindeki tamsayı noktaları ($x=1, 2, 3, ...$) da doğal olarak aynı $L$ çizgisine yaklaşmak zorundadır.

Matematiksel olarak:

$$\text{Eğer } \lim_{x \to \infty} f(x) = L \text{ ise, o zaman } \lim_{n \to \infty} a_n = L \quad (\text{burada } a_n = f(n))$$

#### Bu Teorem Neden Faydalıdır?

Dizilerin limitlerini bulmak için bazen zorlanabiliriz. Ancak bu teorem sayesinde, dizi limitini bir fonksiyon limiti problemine dönüştürebiliriz. Fonksiyon limitleri için kullanabileceğimiz çok daha fazla aracımız var, örneğin **L'Hôpital Kuralı**.

Örnek:

an​=nln(n)​ dizisinin limitini bulmak istediğimizi varsayalım.

1. İlgili Fonksiyonu Tanımla:
    
    an​=f(n) olacak şekilde f(x)=xln(x)​ fonksiyonunu tanımlayalım.
    
2. Fonksiyonun Limitini Hesapla:
    
    Şimdi limx→∞​f(x)'i bulalım. x→∞ iken hem ln(x)→∞ hem de x→∞. Bu bir ∞∞​ belirsizliğidir. Dolayısıyla L'Hôpital Kuralı'nı uygulayabiliriz (pay ve paydanın ayrı ayrı türevini alırız):
    
    $$\lim_{x \to \infty} \frac{\ln(x)}{x} \xrightarrow{\text{L'H}} \lim_{x \to \infty} \frac{\frac{d}{dx}(\ln(x))}{\frac{d}{dx}(x)} = \lim_{x \to \infty} \frac{\frac{1}{x}}{1} = \lim_{x \to \infty} \frac{1}{x} = 0$$
    
3. Teoremi Kullanarak Sonuca Ulaş:
    
    Çünkü limx→∞​f(x)=0 olduğunu bulduk, Teorem 4'e göre ilgili dizinin limiti de aynı olmalıdır:
    
    $$\lim_{n \to \infty} \frac{\ln(n)}{n} = 0$$
    

Umarım bu açıklamalar her iki teoremin de mantığını daha net hale getirmiştir!

Bkz: [[Matematik]] • [[Fizik]]
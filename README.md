XSS (Cross-Site Scripting) Güvenlik Açığı Demosu
Bu repo, siber güvenlik dersi için Cross-Site Scripting (XSS) güvenlik açığını gösteren bir demo projesidir.

Proje İçeriği
Bu projede, basit bir Flask web uygulaması kullanılarak XSS güvenlik açığı gösterilmektedir. Proje, aşağıdaki bileşenleri içerir:

Güvenlik Açığı Olan Kod: vulnerable_xss_app.py - XSS güvenlik açığı içeren yorum sistemi
Düzeltilmiş Kod: fixed_xss_app.py - Bleach kütüphanesi kullanılarak XSS koruması eklenmiş versiyon
Veritabanı Kurulumu: setup_database.py - Demo için veritabanını sıfırlar ve örnek veri ekler
Güvenlik Açığı Bilgileri
OWASP Kategorisi
Bu güvenlik açığı, OWASP Top 10 (2021) listesinde yer alan A03:2021 - Injection kategorisine girmektedir ve spesifik olarak Cross-Site Scripting (XSS) açığıdır.

CVSS Skoru ve Vektör Stringi
CVSS Skoru: 6.1 (Orta)

OWASP Kategorisi: injection -> Stored xss
Vektör Stringi: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N

Bileşenlerin açıklaması:

AV:N - Attack Vector: Network (Saldırı vektörü: Ağ)

AC:L - Attack Complexity: Low (Saldırı karmaşıklığı: Düşük)

PR:N - Privileges Required: None (Gereken ayrıcalıklar: Yok)

UI:R - User Interaction: Required (Kullanıcı etkileşimi: Gerekli)

S:C - Scope: Changed (Kapsam: Değiştirilmiş)

C:L - Confidentiality: Low (Gizlilik etkisi: Düşük)

I:L - Integrity: Low (Bütünlük etkisi: Düşük)

A:N - Availability: None (Kullanılabilirlik etkisi: Yok)
-------------------------------------------------------------------------------
Zafiyet Açıklaması
Cross-Site Scripting (XSS) güvenlik açığı, bir saldırganın kurban kullanıcının tarayıcısında kötü amaçlı JavaScript kodu çalıştırmasına olanak tanır. Bu demoda, kullanıcı yorumları filtre edilmeden veritabanına kaydedilip görüntülendiğinde, kötü amaçlı komut dosyaları diğer kullanıcıların tarayıcısında çalıştırılabilir.

Örnek Saldırı Kodu
<script>alert('XSS!')</script>
Bu kod, güvenlik açığı olan uygulamada bir uyarı penceresi gösterecektir. Daha tehlikeli saldırılarda, bir saldırgan aşağıdaki gibi işlemler yapabilir:

Çerezleri çalabilir
Kullanıcıların hesaplarını ele geçirebilir
Sayfada içerik değiştirebilir
Kullanıcıları sahte sayfalara yönlendirebilir
Demo Videosu
Aşağıdaki videoda, güvenlik açığının nasıl istismar edildiği ve düzeltildiği gösterilmektedir:
-------------------------------------------------------------------------------
Video için buraya tıklayın
-------------------------------------------------------------------------------
Nasıl Çalıştırılır?
Gereksinimleri yükleyin:

pip install flask bleach
Veritabanını kurun:

python setup_database.py
Güvenlik açığı olan uygulamayı çalıştırın:

python vulnerable_xss_app.py
Düzeltilmiş uygulamayı çalıştırın:

python fixed_xss_app.py
Tarayıcınızda http://localhost:5000 adresine gidin ve XSS kodu deneyin.

Nasıl Düzeltildi?
Güvenlik açığı, kullanıcı girdisini HTML kodundan arındıran bleach kütüphanesi kullanılarak düzeltilmiştir. Düzeltilmiş kodda, kullanıcı yorumları veritabanına kaydedilmeden ve görüntülenmeden önce temizlenmektedir.

# XSS Koruması: Kullanıcı girdisini temizliyoruz
clean_name = bleach.clean(name)
clean_comment = bleach.clean(comment)

Referanslar

OWASP XSS Prevention Cheat Sheet

CVSS Calculator

Flask Documentation

Bleach Documentation

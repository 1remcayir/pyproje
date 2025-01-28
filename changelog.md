# Changelog
Alt Alan Adı Tespit Sistemi için tüm önemli değişiklikler bu dosyada belgelenecektir.

Format [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) standardını takip etmektedir,
ve bu proje [Semantic Versioning](https://semver.org/spec/v2.0.0.html) kullanmaktadır.

## [1.0.0] - 2025-01-28
### Eklenenler
- İlk kararlı sürüm yayınlandı
- DNS kayıtlarından alt alan keşfi özelliği
  - Yaygın subdomain listesi desteği
  - Çoklu thread ile paralel tarama
  - Zaman aşımı kontrolleri
- Sertifika şeffaflık logları entegrasyonu
  - crt.sh API entegrasyonu
  - Certspotter API entegrasyonu
- Temel pasif bilgi toplama altyapısı
- Sonuçları metin dosyasına kaydetme özelliği

### Değişenler
- İlk sürüm

### Düzeltilenler
- İlk sürüm

## [0.2.0] - 2025-01-20
### Eklenenler
- Sertifika şeffaflık logları desteği
- Çoklu thread yapısı
- Sonuç kaydetme özelliği

### Değişenler
- DNS sorgu yapısı optimize edildi
- Hata yakalama mekanizması geliştirildi

### Düzeltilenler
- DNS sorguları sırasında oluşan zaman aşımı hataları giderildi
- Bellek kullanımı optimize edildi

## [0.1.0] - 2025-01-15
### Eklenenler
- Proje başlatıldı
- Temel DNS sorgulama fonksiyonları
- Basit komut satırı arayüzü

## Sürüm Numaralandırma Hakkında
- Major sürüm (X.0.0): Geriye dönük uyumsuz API değişiklikleri
- Minor sürüm (0.X.0): Geriye dönük uyumlu yeni özellikler
- Patch sürüm (0.0.X): Geriye dönük uyumlu hata düzeltmeleri

## Etiketler
- [Eklenenler] için yeni özellikler
- [Değişenler] için mevcut işlevlerdeki değişiklikler
- [Düzeltilenler] için hata düzeltmeleri
- [Güvenlik] için güvenlik açığı düzeltmeleri
- [Kaldırılanlar] için kaldırılan özellikler

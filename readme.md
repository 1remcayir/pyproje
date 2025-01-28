# Alt Alan Adı Tespit Sistemi

Bu proje, hedef alan adlarının alt alan adlarını tespit etmek için geliştirilmiş bir Python aracıdır. DNS kayıtları, sertifika şeffaflık logları ve pasif bilgi toplama yöntemlerini kullanarak kapsamlı bir tarama gerçekleştirir.

## Özellikler

- DNS kayıtlarından alt alan keşfi
  - Yaygın subdomain isimlerini otomatik kontrol
  - Paralel tarama ile hızlı sonuç
  - Zaman aşımı kontrolü

- Sertifika Şeffaflık (CT) Loglarından Alt Alan Tespiti
  - crt.sh entegrasyonu
  - Certspotter API desteği
  - Otomatik veri analizi

- Pasif Bilgi Toplama
  - Genişletilebilir yapı
  - Çoklu kaynak desteği
  - Hata yönetimi

## Gereksinimler

```bash
Python 3.8+
dnspython
requests
certifi
urllib3
```

## Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/kullaniciadi/subdomain-scanner.git
cd subdomain-scanner
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

## Kullanım

1. Temel kullanım:
```bash
python subdomain_scanner.py
```

2. Program çalıştığında hedef domain adını girin:
```
Hedef domain adını girin (örn: example.com): example.com
```

3. Sonuçlar otomatik olarak ekrana yazdırılacak ve bir dosyaya kaydedilecektir:
```
[*] example.com için tarama başlatılıyor...
[+] DNS kayıtları taranıyor...
[+] Sertifika şeffaflık logları kontrol ediliyor...
[+] Pasif kaynaklar taranıyor...

Bulunan alt alan adları:
- subdomain1.example.com
- subdomain2.example.com
...
```

## Çıktı Formatı

Sonuçlar iki şekilde sunulur:
1. Terminal ekranında liste halinde
2. `{domain}_subdomains.txt` dosyasında satır satır

## Katkıda Bulunma

1. Bu depoyu fork edin
2. Feature branch'i oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. Bir Pull Request oluşturun

## Geliştirme Yol Haritası

- [ ] Ek pasif bilgi toplama kaynakları ekleme
- [ ] Rate limiting desteği
- [ ] Proxy desteği
- [ ] Farklı çıktı formatları (JSON, CSV)
- [ ] Gelişmiş hata ayıklama seçenekleri
- [ ] Webhook entegrasyonları

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

## İletişim

Proje Sahibi - [@GithubKullaniciAdi](https://github.com/kullaniciadi)

Proje Linki: [https://github.com/kullaniciadi/subdomain-scanner](https://github.com/kullaniciadi/subdomain-scanner)

## Teşekkürler

- [crt.sh](https://crt.sh)
- [CertSpotter](https://certspotter.com)

## Güvenlik

Bu aracı yalnızca izin verilen sistemlerde ve yasal amaçlar için kullanın. Yetkisiz sistem taramaları yasal sonuçlar doğurabilir.

# **BulutVizyon Player**

BulutVizyon Player, Linux tabanlı sistemlerde otomatik olarak bir web tarayıcısını kiosk modunda başlatan ve kullanıcıdan alınan API koduyla dinamik bir URL oluşturup tam ekran bir deneyim sunan bir uygulamadır.

Bu uygulama, özellikle **Orange Pi Lite** ve benzeri cihazlarda kullanılmak üzere tasarlanırmıştır ve minimal ayarlarla kolayca kurulup çalıştırılabilir.

---

## **Özellikler**
- Kullanıcı dostu: Tek bir Python scriptiyle tüm ayarlar yapılır.
- **Chromium** tarayıcısını kiosk modunda başlatır.
- Kullanıcıdan alınan **API koduna** göre URL'yi otomatik oluşturur.
- Sistem açılışında otomatik olarak çalışacak şekilde yapılandırılır.
- SSL sertifika hatalarını devre dışı bırakma ve güvenli tarayıcı parametrelerini içerir.

---

## **Ön Gereksinimler**

BulutVizyon Player'ı kullanmadan önce aşağıdaki gereksinimlerin karşılandığından emin olun:

- **Python 3.6** veya üstü
- **Chromium** tarayıcısı
- Linux tabanlı bir sistem (örneğin, Ubuntu veya Debian)

---

## **Kurulum**

1. **Depoyu Klonlayın**
   ```bash
   git clone https://github.com/kullanici-adi/bulutvizyon-player.git
   cd bulutvizyon-player
   ```

2. **Gerekli Bağımlılıkları Yükleyin**
   Chromium yüklü değilse aşağıdaki komutla yükleyin:
   ```bash
   sudo apt update
   sudo apt install -y chromium-browser
   ```

3. **Scripti Çalıştırın**
   Python scriptini başlatmak için şu komutu çalıştırın:
   ```bash
   python3 setup_autostart.py
   ```

4. **API Kodunuzu Girin**
   Script çalıştırıldığında API kodunuz istenecektir. Bu kod, ilgili URL ile birlikte Chromium tarayıcısında kiosk modunda çalıştırılacaktır.

---

## **Nasıl Çalışır?**

- İlk çalıştırmada, script sizden bir **API kodu** isteyecektir. Bu kod `~/.config/chromium_api_code.txt` dosyasına kaydedilir.
- Script, sistemdeki autostart dosyalarını otomatik olarak oluşturur ve Chromium'u ilgili URL ile başlatacak şekilde ayarlar.
- Sistem her açıldığında Chromium tarayıcısı otomatik olarak başlatılır ve tam ekran modunda çalışır.

---

## **Manuel API Kodu Güncelleme**

Eğer API kodunu değiştirmek isterseniz scripti tekrar çalıştırmanız yeterlidir:
```bash
python3 setup_autostart.py
```

Ya da kaydedilen kodu elle güncelleyebilirsiniz:
```bash
nano ~/.config/chromium_api_code.txt
```

---

## **Kiosk Modu Tarayıcı Parametreleri**

Script tarafından kullanılan Chromium parametreleri:
- `--ignore-certificate-errors`: SSL sertifika hatalarını yok sayar.
- `--disable-web-security`: Tarayıcı güvenliğini devre dışı bırakır.
- `--kiosk`: Tarayıcıyı tam ekran modunda çalıştırır.
- `--disable-infobars`: Gereksiz bilgi çubuklarını devre dışı bırakır.
- `--disable-session-crashed-bubble`: Tarayıcı çökme bildirimlerini kapatır.

---

## **Destek**

BulutVizyon Player hakkında sorularınız veya sorunlarınız için lütfen bizimle iletişime geçin:

- **Web Sitesi:** [bulutvizyon.com](https://bulutvizyon.com)  
- **E-posta:** support@bulutvizyon.com  
- **GitHub Sorun Takibi:** [Issues](https://github.com/kullanici-adi/bulutvizyon-player/issues)

---

## **Katkıda Bulunun**

Proje açık kaynak olarak geliştirilmiştir. Katkıda bulunmak isterseniz şu adımları takip edebilirsiniz:
1. Depoyu fork edin.
2. Yeni bir özellik veya hata düzeltmesi ekleyin.
3. Değişikliklerinizi test edin ve commit edin.
4. Bir pull request açarak katkılarınızı sunun.

---

## **Lisans**

Bu proje MIT lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasını inceleyin.


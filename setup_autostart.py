import os
import shutil
import glob

# API kodunu kaydedeceğimiz dosyanın yolu
API_CODE_FILE = os.path.expanduser("~/.config/luakit_api_code.txt")
AUTOSTART_DIR = os.path.expanduser("~/.config/autostart")
AUTOSTART_FILE = os.path.join(AUTOSTART_DIR, "luakit_autostart.desktop")
SPLASH_IMAGE = "/usr/share/plymouth/themes/pix/splash.png"
BACKUP_SPLASH = "/usr/share/plymouth/themes/pix/splash.png.backup"
LUAKIT_CONFIG_DIR = os.path.expanduser("~/.config/luakit")
LUAKIT_RC_FILE = os.path.join(LUAKIT_CONFIG_DIR, "rc.lua")


def save_api_code(api_code):
    """API kodunu bir dosyaya kaydeder."""
    os.makedirs(os.path.dirname(API_CODE_FILE), exist_ok=True)
    with open(API_CODE_FILE, "w") as f:
        f.write(api_code)


def read_api_code():
    """Kaydedilmiş API kodunu okur."""
    try:
        with open(API_CODE_FILE, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None


def create_luakit_config():
    """Luakit için tam ekran konfigürasyonu oluşturur."""
    os.makedirs(LUAKIT_CONFIG_DIR, exist_ok=True)
    
    # rc.lua dosyası yoksa oluştur
    if not os.path.exists(LUAKIT_RC_FILE):
        with open(LUAKIT_RC_FILE, "w") as f:
            f.write("""-- Luakit konfigürasyon dosyası
local window = require("window")
local webview = require("webview")

-- Başlangıçta tam ekran modunu etkinleştir
window.add_signal("build", function(w)
    w.win.fullscreen = true
end)

-- Web güvenliği ayarlarını devre dışı bırak
webview.add_signal("init", function(view)
    view:toggle_setting("enable-webgl")
    view:toggle_setting("enable-accelerated-compositing")
    view:toggle_setting("hardware-acceleration-policy")
end)
""")
    else:
        # Dosya varsa tam ekran ayarlarını ekle
        with open(LUAKIT_RC_FILE, "r") as f:
            content = f.read()
        
        if "w.win.fullscreen = true" not in content:
            with open(LUAKIT_RC_FILE, "a") as f:
                f.write("""
-- Tam ekran ayarları
window.add_signal("build", function(w)
    w.win.fullscreen = true
end)
""")
    
    print("Luakit konfigürasyonu oluşturuldu.")


def create_autostart_file(api_code):
    """Luakit'i başlatmak için autostart dosyasını oluşturur."""
    # Luakit parametreleri
    url = "https://bulutvizyon.com/viewer/{}".format(api_code)
    luakit_command = "luakit {}".format(url)

    # Autostart dosyasını oluştur
    os.makedirs(AUTOSTART_DIR, exist_ok=True)
    with open(AUTOSTART_FILE, "w") as f:
        f.write(
            """[Desktop Entry]
Type=Application
Exec={}
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=Luakit Auto Start
""".format(luakit_command)
        )
    print("Autostart dosyası oluşturuldu: {}".format(AUTOSTART_FILE))


def change_splash_screen(new_splash_path):
    """Açılış logosunu değiştirir."""
    if os.path.exists(SPLASH_IMAGE):
        # Yedek al
        if not os.path.exists(BACKUP_SPLASH):
            shutil.copy2(SPLASH_IMAGE, BACKUP_SPLASH)
        # Yeni logoyu kopyala
        shutil.copy2(new_splash_path, SPLASH_IMAGE)
        print("Açılış logosu değiştirildi.")
    else:
        print("Hata: Raspberry Pi logo dosyası bulunamadı.")


def find_logo_file():
    """Klasördeki PNG dosyasını bulur."""
    png_files = glob.glob("*.png")
    if png_files:
        return os.path.abspath(png_files[0])
    return None


def main():
    # Daha önce kaydedilmiş bir API kodu var mı kontrol et
    api_code = read_api_code()
    if not api_code:
        # API kodu yoksa kullanıcıdan alın ve kaydedin
        api_code = input("Lütfen API kodunu girin: ")
        save_api_code(api_code)

    # Luakit konfigürasyonu oluştur
    create_luakit_config()
    
    # Autostart dosyasını oluştur
    create_autostart_file(api_code)

    # Açılış logosunu değiştir
    logo_path = find_logo_file()
    if logo_path:
        print(f"Bulunan logo: {logo_path}")
        change_splash_screen(logo_path)
    else:
        print("Klasörde PNG dosyası bulunamadı.")

    print("Sistem açılışında Luakit otomatik olarak başlayacaktır.")


if __name__ == "__main__":
    main()

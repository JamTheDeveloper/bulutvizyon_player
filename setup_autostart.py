import os

# API kodunu kaydedeceğimiz dosyanın yolu
API_CODE_FILE = os.path.expanduser("~/.config/chromium_api_code.txt")
AUTOSTART_DIR = os.path.expanduser("~/.config/autostart")
AUTOSTART_FILE = os.path.join(AUTOSTART_DIR, "chromium_autostart.desktop")


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


def create_autostart_file(api_code):
    """Chromium'u başlatmak için autostart dosyasını oluşturur."""
    # Chromium parametreleri
    url = f"http://168.119.57.127:5005/preview/{api_code}"
    chromium_command = (
        f"chromium-browser --ignore-certificate-errors --disable-web-security "
        f"--kiosk --disable-infobars --disable-session-crashed-bubble {url}"
    )

    # Autostart dosyasını oluştur
    os.makedirs(AUTOSTART_DIR, exist_ok=True)
    with open(AUTOSTART_FILE, "w") as f:
        f.write(
            f"""[Desktop Entry]
Type=Application
Exec={chromium_command}
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=Chromium Auto Start
"""
        )
    print(f"Autostart dosyası oluşturuldu: {AUTOSTART_FILE}")


def main():
    # Daha önce kaydedilmiş bir API kodu var mı kontrol et
    api_code = read_api_code()
    if not api_code:
        # API kodu yoksa kullanıcıdan alın ve kaydedin
        api_code = input("Lütfen API kodunu girin: ")
        save_api_code(api_code)

    # Autostart dosyasını oluştur
    create_autostart_file(api_code)

    print("Sistem açılışında Chromium otomatik olarak başlayacaktır.")


if __name__ == "__main__":
    main()

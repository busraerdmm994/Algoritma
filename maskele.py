def guvenlik_giris_al():
    while True:
        try:
            girdi = input("Lütfen en az 5 haneli bir sayı giriniz: ")
            if len(girdi) >= 5 and girdi.isdigit():
                return int(girdi)
            else:
                print("Geçersiz giriş! Lütfen en az 5 haneli bir pozitif sayı giriniz.")
        except ValueError:
            print("Geçersiz giriş! Lütfen yalnızca sayı giriniz.")

def maskele(girdi):
    girdi_str = str(girdi)
    return "#" * (len(girdi_str) - 4) + girdi_str[-4:]

# Kullanıcıdan girdi al
girdi = guvenlik_giris_al()

# Maskelenmiş çıktı
print("Maskelenmiş çıktı:",maskele(girdi))

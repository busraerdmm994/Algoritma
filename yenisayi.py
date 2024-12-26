sayi = int(input("Lütfen pozitif tam sayı girin: ")) 

if sayi < 0:
    print("Lütfen pozitif tam sayı girin.") 
else:
    rakamlar = [rakam for rakam in str(sayi)]  # Sayıyı string olarak işliyoruz
    rakamlar.sort(reverse=True)               # Rakamları büyükten küçüğe sıralıyoruz
    yeni_sayi = int("".join(rakamlar))        # Sıralı rakamları birleştirip tam sayıya dönüştürüyoruz
    print("Girilen sayının rakamlarından oluşturulan yeni sayı:", yeni_sayi)

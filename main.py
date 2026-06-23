from odunc import OduncKaydi
from kitap import Kitap
from kullanici import Kullanici
from kutuphane import Kutuphane

kutuphane = Kutuphane()

while True:
    print("\nKÜTÜPHANE YÖNETİM SİSTEMİ")
    print("1- Kitap Ekle")
    print("2- Kitapları Listele")
    print("3- Kitap Sil")
    print("4- Kitap Güncelle")
    print("5- Kitap Ara")
    print("6- Kullanıcı Ekle")
    print("7- Kullanıcıları Listele")
    print("8- Kitap Ödünç Ver")
    print("9- Kitap İade Et")
    print("10- Ödünç Kayıtlarını Listele")
    print("11- Çıkış")

    secim = input("Seçiminiz: ")

    try:
        if secim == "1":
            id = int(input("Kitap ID: "))
            ad = input("Kitap Adı: ")
            yazar = input("Yazar: ")
            kategori = input("Kategori: ")
            yayin_yili = int(input("Yayın Yılı: "))

            yeni_kitap = Kitap(id, ad, yazar, kategori, yayin_yili)
            kutuphane.kitap_ekle(yeni_kitap)
        

        elif secim == "2":
            kutuphane.kitaplari_listele()

        elif secim == "3":
            kitap_id = int(input("Silinecek Kitap ID: "))
            kutuphane.kitap_sil(kitap_id)

        elif secim == "4":
            kitap_id = int(input("Güncellenecek Kitap ID: "))
            kutuphane.kitap_guncelle(kitap_id)

        elif secim == "5":
            aranacak_ad = input("Aranacak kitap adı: ")
            kutuphane.kitap_ara(aranacak_ad)

        elif secim == "6":
            id = int(input("Kullanıcı ID: "))
            ad_soyad = input("Ad Soyad: ")
            ogrenci_no = input("Öğrenci No: ")

            yeni_kullanici = Kullanici(id, ad_soyad, ogrenci_no)
            kutuphane.kullanici_ekle(yeni_kullanici)

        elif secim == "7":
            kutuphane.kullanicilari_listele()

        elif secim == "8":
            kayit_id = int(input("Kayıt ID: "))
            kitap_id = int(input("Kitap ID: "))
            kullanici_id = int(input("Kullanıcı ID: "))
            alis_tarihi = input("Alış Tarihi: ")

            odunc = OduncKaydi(kayit_id, kitap_id, kullanici_id, alis_tarihi)
            kutuphane.kitap_odunc_ver(odunc)

        elif secim == "9":
            kayit_id = int(input("İade edilecek kayıt ID: "))
            kutuphane.kitap_iade_et(kayit_id)

        elif secim == "10":
            kutuphane.odunc_kayitlarini_listele()

        elif secim == "11":
            print("Programdan çıkılıyor...")
            break

        else:
            print("Geçersiz seçim yaptınız.")

    except ValueError:
        print("Hatalı giriş yaptınız. Lütfen sayı gereken alanlara sayı giriniz.")
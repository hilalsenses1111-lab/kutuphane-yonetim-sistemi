import json
from kitap import Kitap
from kullanici import Kullanici
from odunc import OduncKaydi


class Kutuphane:
    def __init__(self):
        self.kitaplar = []
        self.kullanicilar = []
        self.odunc_kayitlari = []
        self.verileri_yukle()

    def kitap_ekle(self, kitap):
        for mevcut_kitap in self.kitaplar:
            if mevcut_kitap.id == kitap.id:
                print("Bu ID ile kayıtlı bir kitap zaten var.")
                return

        self.kitaplar.append(kitap)
        self.verileri_kaydet()
        print("Kitap başarıyla eklendi.")

    def kitaplari_listele(self):
        if not self.kitaplar:
            print("Kayıtlı kitap bulunmamaktadır.")
        else:
            for kitap in self.kitaplar:
                kitap.bilgi_goster()
                print("-" * 20)

    def kitap_sil(self, kitap_id):
        for kitap in self.kitaplar:
            if kitap.id == kitap_id:
                self.kitaplar.remove(kitap)
                self.verileri_kaydet()
                print("Kitap başarıyla silindi.")
                return
        print("Bu ID'ye sahip kitap bulunamadı.")

    def kitap_guncelle(self, kitap_id):
        for kitap in self.kitaplar:
            if kitap.id == kitap_id:
                kitap.ad = input("Yeni kitap adı: ")
                kitap.yazar = input("Yeni yazar: ")
                kitap.kategori = input("Yeni kategori: ")
                kitap.yayin_yili = int(input("Yeni yayın yılı: "))
                self.verileri_kaydet()
                print("Kitap başarıyla güncellendi.")
                return
        print("Bu ID'ye sahip kitap bulunamadı.")

    def kitap_ara(self, aranacak_ad):
        bulundu = False
        for kitap in self.kitaplar:
            if aranacak_ad.lower() in kitap.ad.lower():
                kitap.bilgi_goster()
                print("-" * 20)
                bulundu = True
        if not bulundu:
            print("Kitap bulunamadı.")

    def kullanici_ekle(self, kullanici):
        for mevcut_kullanici in self.kullanicilar:
            if mevcut_kullanici.id == kullanici.id:
                print("Bu ID ile kayıtlı bir kullanıcı zaten var.")
                return

        self.kullanicilar.append(kullanici)
        self.verileri_kaydet()
        print("Kullanıcı başarıyla eklendi.")

    def kullanicilari_listele(self):
        if not self.kullanicilar:
            print("Kayıtlı kullanıcı bulunmamaktadır.")
        else:
            for kullanici in self.kullanicilar:
                kullanici.bilgi_goster()
                print("-" * 20)

    def kitap_odunc_ver(self, odunc):
        kullanici_var_mi = False

        for kullanici in self.kullanicilar:
            if kullanici.id == odunc.kullanici_id:
                kullanici_var_mi = True
                break

        if not kullanici_var_mi:
            print("Bu ID'ye sahip kullanıcı bulunamadı.")
            return

        for kitap in self.kitaplar:
            if kitap.id == odunc.kitap_id:
                if not kitap.mevcut_mu:
                    print("Kitap zaten ödünç verilmiş.")
                    return

                kitap.mevcut_mu = False
                self.odunc_kayitlari.append(odunc)
                self.verileri_kaydet()
                print("Kitap başarıyla ödünç verildi.")
                return

        print("Kitap bulunamadı.")

    def odunc_kayitlarini_listele(self):
        if not self.odunc_kayitlari:
            print("Ödünç kaydı bulunmamaktadır.")
        else:
            for kayit in self.odunc_kayitlari:
                kayit.durum_goster()
                print("-" * 20)

    def kitap_iade_et(self, kayit_id):
        for kayit in self.odunc_kayitlari:
            if kayit.id == kayit_id:
                if kayit.iade_edildi:
                    print("Bu kitap zaten iade edilmiş.")
                    return

                kayit.iade_edildi = True

                for kitap in self.kitaplar:
                    if kitap.id == kayit.kitap_id:
                        kitap.mevcut_mu = True
                        break

                self.verileri_kaydet()
                print("Kitap başarıyla iade edildi.")
                return

        print("Kayıt bulunamadı.")

    def verileri_kaydet(self):
        veri = {
            "kitaplar": [
                {
                    "id": kitap.id,
                    "ad": kitap.ad,
                    "yazar": kitap.yazar,
                    "kategori": kitap.kategori,
                    "yayin_yili": kitap.yayin_yili,
                    "mevcut_mu": kitap.mevcut_mu
                }
                for kitap in self.kitaplar
            ],
            "kullanicilar": [
                {
                    "id": kullanici.id,
                    "ad_soyad": kullanici.ad_soyad,
                    "ogrenci_no": kullanici.ogrenci_no
                }
                for kullanici in self.kullanicilar
            ],
            "odunc_kayitlari": [
                {
                    "id": kayit.id,
                    "kitap_id": kayit.kitap_id,
                    "kullanici_id": kayit.kullanici_id,
                    "alis_tarihi": kayit.alis_tarihi,
                    "teslim_tarihi": kayit.teslim_tarihi,
                    "iade_edildi": kayit.iade_edildi
                }
                for kayit in self.odunc_kayitlari
            ]
        }

        with open("data.json", "w", encoding="utf-8") as dosya:
            json.dump(veri, dosya, ensure_ascii=False, indent=4)

    def verileri_yukle(self):
        try:
            with open("data.json", "r", encoding="utf-8") as dosya:
                veri = json.load(dosya)

                for kitap_verisi in veri["kitaplar"]:
                    kitap = Kitap(
                        kitap_verisi["id"],
                        kitap_verisi["ad"],
                        kitap_verisi["yazar"],
                        kitap_verisi["kategori"],
                        kitap_verisi["yayin_yili"]
                    )
                    kitap.mevcut_mu = kitap_verisi["mevcut_mu"]
                    self.kitaplar.append(kitap)

                for kullanici_verisi in veri["kullanicilar"]:
                    kullanici = Kullanici(
                        kullanici_verisi["id"],
                        kullanici_verisi["ad_soyad"],
                        kullanici_verisi["ogrenci_no"]
                    )
                    self.kullanicilar.append(kullanici)

                for kayit_verisi in veri["odunc_kayitlari"]:
                    kayit = OduncKaydi(
                        kayit_verisi["id"],
                        kayit_verisi["kitap_id"],
                        kayit_verisi["kullanici_id"],
                        kayit_verisi["alis_tarihi"]
                    )
                    kayit.teslim_tarihi = kayit_verisi["teslim_tarihi"]
                    kayit.iade_edildi = kayit_verisi["iade_edildi"]
                    self.odunc_kayitlari.append(kayit)

        except FileNotFoundError:
            self.verileri_kaydet()

        except json.JSONDecodeError:
            self.verileri_kaydet()
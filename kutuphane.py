from kitap import Kitap
from kullanici import Kullanici
from odunc import OduncKaydi


class Kutuphane:
    def __init__(self):
        self.kitaplar = []
        self.kullanicilar = []
        self.odunc_kayitlari = []

    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)

    def kitaplari_listele(self):
        for kitap in self.kitaplar:
            kitap.bilgi_goster()
            print("-" * 20)
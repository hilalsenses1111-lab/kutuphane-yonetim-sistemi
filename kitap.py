class Kitap:
    def __init__(self, id, ad, yazar, kategori, yayin_yili):
        self.id = id
        self.ad = ad
        self.yazar = yazar
        self.kategori = kategori
        self.yayin_yili = yayin_yili
        self.mevcut_mu = True

    def bilgi_goster(self):
        print(f"ID: {self.id}")
        print(f"Ad: {self.ad}")
        print(f"Yazar: {self.yazar}")
        print(f"Kategori: {self.kategori}")
        print(f"Yayın Yılı: {self.yayin_yili}")
        print(f"Durum: {'Mevcut' if self.mevcut_mu else 'Ödünçte'}")
class Kullanici:
    def __init__(self, id, ad_soyad, ogrenci_no):
        self.id = id
        self.ad_soyad = ad_soyad
        self.ogrenci_no = ogrenci_no

    def bilgi_goster(self):
        print(f"ID: {self.id}")
        print(f"Ad Soyad: {self.ad_soyad}")
        print(f"Öğrenci No: {self.ogrenci_no}")
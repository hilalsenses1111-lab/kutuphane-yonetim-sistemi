class OduncKaydi:
    def __init__(self, id, kitap_id, kullanici_id, alis_tarihi):
        self.id = id
        self.kitap_id = kitap_id
        self.kullanici_id = kullanici_id
        self.alis_tarihi = alis_tarihi
        self.teslim_tarihi = None
        self.iade_edildi = False

    def durum_goster(self):
        print(f"Kayıt ID: {self.id}")
        print(f"Kitap ID: {self.kitap_id}")
        print(f"Kullanıcı ID: {self.kullanici_id}")
        print(f"Alış Tarihi: {self.alis_tarihi}")
        print(f"Teslim Tarihi: {self.teslim_tarihi}")
        print(f"İade Edildi: {self.iade_edildi}")
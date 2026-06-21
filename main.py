from kitap import Kitap
from kutuphane import Kutuphane

kutuphane = Kutuphane()

kitap1 = Kitap(1, "Sefiller", "Victor Hugo", "Roman", 1862)
kitap2 = Kitap(2, "Suç ve Ceza", "Dostoyevski", "Roman", 1866)

kutuphane.kitap_ekle(kitap1)
kutuphane.kitap_ekle(kitap2)

print("KÜTÜPHANE YÖNETİM SİSTEMİ")
print("-" * 30)

kutuphane.kitaplari_listele()
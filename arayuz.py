import tkinter as tk
from tkinter import ttk, messagebox

from kitap import Kitap
from kutuphane import Kutuphane

kutuphane = Kutuphane()

pencere = tk.Tk()
pencere.title("Kütüphane Yönetim Sistemi")
pencere.geometry("950x600")
pencere.configure(bg="#f1f5f9")

# SOL MENÜ
sol_menu = tk.Frame(pencere, bg="#1e293b", width=220)
sol_menu.pack(side="left", fill="y")

baslik = tk.Label(
    sol_menu,
    text="KÜTÜPHANE\nYÖNETİM\nSİSTEMİ",
    bg="#1e293b",
    fg="white",
    font=("Arial", 17, "bold")
)
baslik.pack(pady=30)

# SAĞ ALAN
icerik = tk.Frame(pencere, bg="#f1f5f9")
icerik.pack(side="right", expand=True, fill="both")

ust_baslik = tk.Label(
    icerik,
    text="Kitap Yönetim Paneli",
    bg="#f1f5f9",
    fg="#0f172a",
    font=("Arial", 24, "bold")
)
ust_baslik.pack(pady=20)

# FORM ALANI
form = tk.Frame(icerik, bg="#f1f5f9")
form.pack(pady=10)

tk.Label(form, text="ID", bg="#f1f5f9").grid(row=0, column=0, padx=5)
tk.Label(form, text="Kitap Adı", bg="#f1f5f9").grid(row=0, column=1, padx=5)
tk.Label(form, text="Yazar", bg="#f1f5f9").grid(row=0, column=2, padx=5)
tk.Label(form, text="Kategori", bg="#f1f5f9").grid(row=0, column=3, padx=5)
tk.Label(form, text="Yayın Yılı", bg="#f1f5f9").grid(row=0, column=4, padx=5)

id_entry = tk.Entry(form, width=8)
ad_entry = tk.Entry(form, width=18)
yazar_entry = tk.Entry(form, width=18)
kategori_entry = tk.Entry(form, width=15)
yil_entry = tk.Entry(form, width=10)

id_entry.grid(row=1, column=0, padx=5)
ad_entry.grid(row=1, column=1, padx=5)
yazar_entry.grid(row=1, column=2, padx=5)
kategori_entry.grid(row=1, column=3, padx=5)
yil_entry.grid(row=1, column=4, padx=5)

# TABLO
kolonlar = ("ID", "Ad", "Yazar", "Kategori", "Yıl", "Durum")
tablo = ttk.Treeview(icerik, columns=kolonlar, show="headings", height=15)

for kolon in kolonlar:
    tablo.heading(kolon, text=kolon)
    tablo.column(kolon, width=120)

tablo.pack(pady=20, padx=20, fill="x")


def tabloyu_yenile():
    for satir in tablo.get_children():
        tablo.delete(satir)

    for kitap in kutuphane.kitaplar:
        durum = "Mevcut" if kitap.mevcut_mu else "Ödünçte"
        tablo.insert(
            "",
            "end",
            values=(kitap.id, kitap.ad, kitap.yazar, kitap.kategori, kitap.yayin_yili, durum)
        )


def kitap_ekle():
    try:
        yeni_kitap = Kitap(
            int(id_entry.get()),
            ad_entry.get(),
            yazar_entry.get(),
            kategori_entry.get(),
            int(yil_entry.get())
        )

        kutuphane.kitap_ekle(yeni_kitap)
        tabloyu_yenile()

        id_entry.delete(0, tk.END)
        ad_entry.delete(0, tk.END)
        yazar_entry.delete(0, tk.END)
        kategori_entry.delete(0, tk.END)
        yil_entry.delete(0, tk.END)

        messagebox.showinfo("Başarılı", "Kitap ekleme işlemi tamamlandı.")

    except ValueError:
        messagebox.showerror("Hata", "ID ve Yayın Yılı sayı olmalıdır.")


def kitap_sil():
    secili = tablo.selection()

    if not secili:
        messagebox.showwarning("Uyarı", "Silmek için bir kitap seçiniz.")
        return

    kitap_id = int(tablo.item(secili[0])["values"][0])
    kutuphane.kitap_sil(kitap_id)
    tabloyu_yenile()
    messagebox.showinfo("Başarılı", "Kitap silindi.")


def kitap_ara():
    aranan = ad_entry.get().lower()

    for satir in tablo.get_children():
        tablo.delete(satir)

    for kitap in kutuphane.kitaplar:
        if aranan in kitap.ad.lower():
            durum = "Mevcut" if kitap.mevcut_mu else "Ödünçte"
            tablo.insert(
                "",
                "end",
                values=(kitap.id, kitap.ad, kitap.yazar, kitap.kategori, kitap.yayin_yili, durum)
            )


def tumunu_goster():
    tabloyu_yenile()


# BUTONLAR
tk.Button(sol_menu, text="Kitap Ekle", bg="#2563eb", fg="white", width=20, height=2,
          command=kitap_ekle).pack(pady=8)

tk.Button(sol_menu, text="Kitap Sil", bg="#dc2626", fg="white", width=20, height=2,
          command=kitap_sil).pack(pady=8)

tk.Button(sol_menu, text="Kitap Ara", bg="#16a34a", fg="white", width=20, height=2,
          command=kitap_ara).pack(pady=8)

tk.Button(sol_menu, text="Tümünü Göster", bg="#9333ea", fg="white", width=20, height=2,
          command=tumunu_goster).pack(pady=8)

tk.Button(sol_menu, text="Çıkış", bg="#111827", fg="white", width=20, height=2,
          command=pencere.destroy).pack(pady=30)

tabloyu_yenile()
pencere.mainloop()
from prettytable import PrettyTable
from data import tukang

def tampil_paket(daftar, hanya_tersedia):
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama", "Harga/m2", "Fitur", "Butuh", "Sedia"]
    for i in range(len(daftar)):
        if hanya_tersedia and not daftar[i]["sedia"]:
            continue
        tabel.add_row([i + 1, daftar[i]["nama"], daftar[i]["harga"], daftar[i]["fitur"],
                       daftar[i].get("membutuhkan", "-"), "Ya" if daftar[i]["sedia"] else "Tidak"])
    if len(tabel.rows) == 0:
        print("Paket sedang habis semua.")
    else:
        print(tabel)

def tampil_tukang():
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama", "Status"]
    for i in range(len(tukang)):
        tabel.add_row([i + 1, tukang[i]["nama"], tukang[i]["status"]])
    if len(tabel.rows) == 0:
        print("Belum ada tukang.")
    else:
        print(tabel)

def tampil_pesanan(daftar, admin=False):
    tabel = PrettyTable()
    kolom = ["No"]
    if admin:
        kolom.append("Pelanggan")
    kolom += ["Paket", "Lokasi", "Tukang", "Total", "Pembayaran", "Status"]
    tabel.field_names = kolom
    for o in daftar:
        baris = [o["no_pesanan"]]
        if admin:
            baris.append(o["username"])
        baris += [o["paket"], o["lokasi"], ", ".join(o["nama_tukang"]), o["total"], o["pembayaran"], o["status"]]
        tabel.add_row(baris)
    if len(tabel.rows) == 0:
        print("Belum ada pesanan.")
    else:
        print(tabel)
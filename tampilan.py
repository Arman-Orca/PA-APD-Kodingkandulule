from prettytable import PrettyTable
from data import tukang
def tampil_paket(daftar, hanya_tersedia):
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama", "Harga", "Fitur", "Sedia"]
    for i in range(len(daftar)):
        if hanya_tersedia and not daftar[i]["sedia"]:
            continue
        tabel.add_row([i + 1, daftar[i]["nama"], daftar[i]["harga"], daftar[i]["fitur"], "Ya" if daftar[i]["sedia"] else "Tidak"])
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
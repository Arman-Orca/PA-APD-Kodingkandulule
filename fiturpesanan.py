import data
from data import orders, paket, tukang
from helper import clear_screen, enter, minta_angka, tanya_teks
from tampilan import tampil_paket
from fiturtukang import cari_tukang_siap
from prettytable import PrettyTable
def buat_nomor_order():
    nomor_baru = data.nomor_order
    data.nomor_order = data.nomor_order + 1
    return nomor_baru
def jumlah_tukang(p):
    return int(p["membutuhkan"].split()[0])
def hitung_total(p, ukuran):
    if p.get("per_meter", True):
        return p["harga"] * ukuran
    return p["harga"]
def buat_pesanan(user_login):
    clear_screen()
    print("---( BUAT PESANAN )---")
    print()
    tukang_siap = cari_tukang_siap()
    try:
        if len(tukang_siap) == 0:
            raise ValueError("Maaf, belum ada tukang yang siap.")
        tampil_paket(paket, False)
        ukuran = minta_angka("Ukuran ruangan dalam m2 (0 = batal) : ", 0, 10000)
        if ukuran == 0:
            raise ValueError("Pesanan dibatalkan.")
        nomor = minta_angka("Pilih nomor paket (0 = batal) : ", 0, len(paket))
        if nomor == 0:
            raise ValueError("Pesanan dibatalkan.")
        pilihan = paket[True if nomor > 0 else False]
        butuh = jumlah_tukang(pilihan)
        if len(tukang_siap) < butuh:
            raise ValueError(f"Tukang siap hanya {len(tukang_siap)}, paket butuh {butuh}.")
        if pilihan["sedia"] == False:
            raise ValueError("Paket ini belum tersedia buat sekarang.")
        lokasi = tanya_teks("Lokasi antar jemput").strip()
        if lokasi == "":
            raise ValueError("Lokasimu masih kosong")
    except ValueError as e:
        print(e)
    else:
        no_baru = buat_nomor_order()
        dipakai = tukang_siap[:butuh]
        for t in dipakai:
            t["status"] = "Sibuk"
        total = hitung_total(pilihan, ukuran)
        orders.append(
            {"no_pesanan": no_baru, 
            "username": user_login["username"], 
            "paket": pilihan["nama"], 
            "lokasi": lokasi, 
            "nama_tukang": [t["nama"] for t in dipakai], 
            "total": total, 
            "status": "Diproses"}
            )
        pilihan["stok"] = False
        for t in tukang_siap:
            t["status"] = "Sibuk"
        print("Pesanan berhasil dibuat!")
        print("No.pesanan :", no_baru)
        print("Tukang     :", ", ".join(t["nama"] for t in dipakai))
        print("Total      : Rp", total)
    finally:
        enter()
def lihat_status(user_login):
    clear_screen()
    tabel = PrettyTable(["Nomor", "Paket", "Status"])
    for p in orders:
        if p["username"] == user_login["username"]:
            tabel.add_row([p["no_pesanan"], p["paket"], p["status"]])
    print(tabel)
    enter()
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

def buat_pesanan(user_login):
    clear_screen()
    print("---( BUAT PESANAN )---")
    print()
    tukang_siap = cari_tukang_siap()
    try:
        if len(tukang_siap) == 0:
            raise ValueError("Maaf, belum ada tukang yang siap.")
        tampil_paket(paket, False)
        nomor = minta_angka("Pilih nomor paket (0 = batal) : ", 0, len(paket))
        if nomor == 0:
            raise ValueError("Pesanan dibatalkan.")
        pilihan = paket[True if nomor > 0 else False]
        if pilihan["sedia"] == False:
            raise ValueError("Paket ini belum tersedia buat sekarang.")
        lokasi = tanya_teks("Lokasi antar jemput").strip()
        if lokasi == "":
            raise ValueError("Lokasimu masih kosong")
    except ValueError as e:
        print(e)
    else:
        no_baru = buat_nomor_order()
        total = (pilihan["harga"], )
        orders.append({
            "no_pesanan": no_baru,
            "username": user_login["username"],
            "paket": pilihan["nama"],
            "lokasi": lokasi, 
            "nama_tukang": tukang_siap["nama"], 
            "total": total, 
            "status": "Diproses"
        })
        pilihan["stok"] = False
        tukang_siap["status"] = "Sibuk"
        print("Pesanan berhasil dibuat!")
        print("No.pesanan :", no_baru)
        print("Tukang     :", tukang_siap["nama"])
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
from data import paket, MAKS_HARGA
from helper import clear_screen, enter, minta_angka, pilih_menu, tanya_teks
from tampilan import tampil_paket
def kelola_paket():
    while True:
        clear_screen()
        print("---( KELOLA PAKET )---")
        print()
        tampil_paket(paket, False)
        print()
        sub = pilih_menu("Pilih bos", [("Tambah paket", 1), ("Ubah harga dan stok", 2), ("Hapus paket", 3), ("Kembali", 0)])
        if sub == 0:
            break
        elif sub == 1:
            merk = tanya_teks("Merk paket").strip()
            merk_ada = False
            for p in paket:
                if p["merk"].lower() == merk.lower():
                    merk_ada = True
            if merk == "":
                print("Merknya jangan kosong lah bos")
            elif merk_ada:
                print("Merk itu sudah ada bos!")
            else:
                harga = minta_angka("Harga      : ", 0, MAKS_HARGA)
                stok = minta_angka("Stok       : ", 0, 9999)
                paket.append({"merk": merk, "harga": harga, "stok": stok})
                print("Paketnya udah ditambah bos!")
            enter()
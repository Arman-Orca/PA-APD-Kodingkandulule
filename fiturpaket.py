from data import paket, MAKS_HARGA
from helper import clear_screen, enter, pilih_menu, tanya_teks
from tampilan import tampil_paket
from fiturtukang import ambil_nomor

def minta_angka(pesan, minimal, maksimal):
    while True:
        try:
            nilai = int(tanya_teks(pesan))
            if nilai < minimal or nilai > maksimal:
                raise ValueError
        except ValueError:
            print("Isi angka bulat", minimal, "sampai", maksimal)
        else:
            return nilai
        
def kelola_paket():
    while True:
        clear_screen()
        print("---( KELOLA PAKET )---")
        print()
        tampil_paket(paket, False)
        print()
        sub = pilih_menu("Pilih", [("Tambah paket", 1), ("Ubah paket", 2), ("Ubah status paket", 3), ("Kembali", 0)])
        if sub == 0:
            break
        elif sub == 1:
            nama = tanya_teks("Nama paket").strip()
            nama_ada = False
            for p in paket:
                if p["nama"].lower() == nama.lower():
                    nama_ada = True
            if nama == "":
                print("Nama nggak boleh kosong!")
            elif nama_ada:
                print("Nama sudah ada!")
            else:
                harga = minta_angka("Harga : ", 0, MAKS_HARGA)
                fitur = minta_angka("Fitur : ", 0, 999)
                paket.append({"nama": nama, "harga": harga, "fitur": fitur, "sedia": True})
                print("Paketnya udah ditambah!")
            enter()
        elif sub == 2:
            if len(paket) == 0:
                print("Belum ada paket!")
                enter()
                continue
            idx = ambil_nomor(paket)
            if idx is None:
                enter()
                continue
            nama = tanya_teks("Nama baru").strip()
            nama_ada = False
            for i in range(len(paket)):
                if i != idx and paket[i]["nama"].lower() == nama.lower():
                    nama_ada = True
            if nama == "":
                print("Nama nggak boleh kosong!")
            elif nama_ada:
                print("Nama itu sudah ada!")
            else:
                harga = minta_angka("Harga baru : ", 0, MAKS_HARGA)
                fitur = tanya_teks("Fitur baru").strip()
                paket[idx]["nama"] = nama
                paket[idx]["harga"] = harga
                paket[idx]["fitur"] = fitur
                print("Paketnya udah diubah!")
            enter()
        elif sub == 3:
            if len(paket) == 0:
                print("Belum ada paket!")
                enter()
                continue
            idx = ambil_nomor(paket)
            if idx is None:
                enter()
                continue
            status = pilih_menu("Status baru", [("Tersedia", True), ("Habis", False)])
            paket[idx]["sedia"] = status
            print("Status", paket[idx]["nama"], "udah jadi", "Tersedia" if status else "Habis")
            enter()